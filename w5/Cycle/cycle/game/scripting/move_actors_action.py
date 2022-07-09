from game.scripting.action import Action


# TODO: Implement MoveActorsAction class here! 
class MoveActorsAction(Action):

# Override the execute(cast, script) method as follows:
    def execute(self, cast, script):
        actors = cast.get_all_actors()
        snake = cast.get_first_actor("snakes")
        snake2 = cast.get_first_actor("snake2")

        for actor in actors:
        
            actor.move_next()
# 1) get all the actors from the cast
# 2) loop through the actors
# 3) call the move_next() method on each actor