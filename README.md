# HKX Animation for Blender 5.1+

This is an updated version of the [blender-hkx](https://github.com/jgernandt/blender-hkx) addon originally created by Jonas Gernandt. It has been migrated to support Blender 4.0 ~ 5.1 and its new Slotted Action API.

## Updates in this version (by Smooth)
- **Blender 5.1 compatibility**: Fixed issues with the new Layered/Slotted Action system.
- **Bone Grouping**: Restored bone F-Curve grouping within the Action Editor using the new `ActionGroup` API.
- **Auto FPS Setting**: Automatically detects and sets the scene frame rate to 30 FPS upon import (Havok standard).
- **Bug Fixes**: Resolved various `AttributeError` and `NameError` issues caused by API changes in Blender 4.0+.

## Important: Requirements
This addon **does not include** the Havok converter executable (`blender-hkx.exe`) due to licensing restrictions.

To use this addon, you must:
1. Obtain `blender-hkx.exe` (built from the original [source code](https://github.com/jgernandt/blender-hkx)).
2. Install the addon in Blender.
3. In the Addon Preferences, set the path to your `blender-hkx.exe`.

## Installation
1. Download `io_hkx_animation.zip` from the Releases page.
2. In Blender, go to `Edit > Preferences > Addons > Install...` and select the zip file.
3. Enable "HKX Animation" and configure the converter path in the preferences.

## Credits
- **Jonas Gernandt**: Original author of the blender-hkx addon.
- **Smooth**: Migration to Blender 5.1 and general maintenance.
