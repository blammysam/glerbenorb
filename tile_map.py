import tiles

class TileMap:
    character_tiles = {"g":tiles.GroundTile,"w":tiles.WallTile}
    def __init__(self, map_string):
        self.tiles = []
        #split the string into an array of lines
        map_string = map_string.split("!")
        #remove line breaks from each line
        for i in range(len(map_string)):
            map_string[i] = map_string[i].replace("\n","")
            #create a new tile based on each character in each line
            for j,character in enumerate(map_string[i]):
                new_tile = TileMap.character_tiles[character](j,i)
                self.tiles.append(new_tile)