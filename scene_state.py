class SceneState:
    scene_state = "title"

    def set_scene_state(new_state):
        SceneState.scene_state = new_state
    def get_scene_state():
        return SceneState.scene_state