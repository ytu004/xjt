"""Run once with UnrealEditor-Cmd -run=pythonscript -script=<this file>."""
import unreal

MAP = "/Game/XJT/Maps/L_Prototype"
if unreal.EditorAssetLibrary.does_asset_exist(MAP):
    raise RuntimeError("Initial map already exists; refusing to overwrite it.")

levels = unreal.get_editor_subsystem(unreal.LevelEditorSubsystem)
actors = unreal.get_editor_subsystem(unreal.EditorActorSubsystem)
if not levels.new_level(MAP):
    raise RuntimeError("Could not create prototype map")

cube = unreal.load_asset("/Engine/BasicShapes/Cube.Cube")
assert cube is not None
for index, (x, z, width) in enumerate([(0, 0, 6), (650, 100, 3), (1150, 180, 3), (1650, 100, 4)]):
    actor = actors.spawn_actor_from_class(unreal.StaticMeshActor, unreal.Vector(x, 0, z))
    actor.set_actor_label("Platform_%02d" % index)
    actor.static_mesh_component.set_static_mesh(cube)
    actor.set_actor_scale3d(unreal.Vector(width, 2, 0.4))

start = actors.spawn_actor_from_class(unreal.PlayerStart, unreal.Vector(0, 0, 150))
start.set_actor_label("PlayerStart_Prototype")
light = actors.spawn_actor_from_class(unreal.DirectionalLight, unreal.Vector(0, 0, 600), unreal.Rotator(-45, -30, 0))
light.set_actor_label("Prototype_Sun")
light.light_component.set_editor_property("intensity", 5.0)
sky = actors.spawn_actor_from_class(unreal.SkyLight, unreal.Vector(0, 0, 500))
sky.set_actor_label("Prototype_SkyLight")
if not levels.save_current_level():
    raise RuntimeError("Could not save prototype map")
unreal.log("XJT_INITIAL_MAP_CREATED")
