"""Validate the saved project foundation using Unreal's editor commandlet."""
import unreal

levels = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
assert levels.load_level("/Game/XJT/Maps/L_Prototype"), "Map cannot be loaded"
actors = unreal.get_editor_subsystem(unreal.EditorActorSubsystem).get_all_level_actors()
platforms = [actor for actor in actors if actor.get_actor_label().startswith("Platform_")]
assert len(platforms) == 4, "Expected four greybox platforms"
assert all(actor.static_mesh_component.static_mesh is not None for actor in platforms)
assert any(isinstance(actor, unreal.PlayerStart) for actor in actors), "Missing PlayerStart"
unreal.log("XJT_PROJECT_VALIDATION_PASSED")
