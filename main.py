import tcod

from engine import Engine
from entity import Entity
from input_handlers import EventHandler
from procgen import generate_dungeon

def main() -> None:

    w, h = 100, 100

    map_w, map_h = 100, 100

    room_max_size = 10
    room_min_size = 6
    max_rooms = 30

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
        ) # TCOD commands to get font style
    
    event_handler = EventHandler()

    player = Entity(int(w / 2), int(h / 2), "@", (255, 255, 255))
    npc = Entity(int(w / 2 - 5), int(h / 2), "@", (255, 255, 0))
    entities = {npc, player}

    game_map = generate_dungeon(
        max_rooms=max_rooms,
        room_min_size=room_min_size,
        room_max_size=room_max_size,
        map_width=map_w,
        map_height=map_h,
        player=player
    )

    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)
    with tcod.context.new_terminal(
        w, h, tileset=tileset, title="Roguelike", vsync=True,
    ) as context: # Creating screen
        root_console = tcod.Console(w, h, order="F") # Console to draw to; order F to revese x and y
        while True:
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)
            
if __name__ == "__main__":
    main()