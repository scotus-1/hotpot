 (pre-generate large world and view with map viewer or /structure-list or smth)
11. fcsp++ -  tweak structure generation and disable some
12. fcsp++ - tweak biome generation

13. server setup!
- https://blogs.oracle.com/developers/post/how-to-set-up-and-run-a-really-powerful-free-minecraft-server-in-the-cloud
- https://minecraft.fandom.com/wiki/Tutorials/Setting_up_a_server
- https://github.com/brucethemoose/Minecraft-Performance-Flags-Benchmarks

CLIENT-SIDE:
- Remove certain Icons splashes and merge with vanilla
- Reduce blocklight flicker
- Mark e4mc as client-only
- Update Complementary


SERVER-SIDE:
- Handcrafted block entity models not rendering (remove better beds)
- Sleepwarp incompat with time and wind
- readd EBE?
- Floating shipwreck structure?

BOTH-SIDES:
- Create modlists
- Update all mods before release
- Update .zip distribution files
- Versioned Releases for stability

SERVER:
- Find good seed
- Set up Proximity Voice Chat
- Set up Create Track Map
- Set up Dynmap
- Set up docker based backups
- Set up Discord Integration
- Readd CC to test if working

PORTS TO OPEN:
- 25565 tcp/udp
- 3876 tcp (CTM)
- 24454 udp (SVC)
- 8123 tcp (Dynmap)

FOR DYNMAP:
-Dloader.workaround.jar_copied_mods=dynmap

Repurposed Structures: Failed to create valid structure with all required pieces starting from this pool file: repurposed_structures:villages/mountains/town_centers. Required pieces failed to generate the required amount are: [fwaystones:stone_brick_village_waystone=1]
  This can happen if a structure has a required piece but the structure size is set too low.
  However, this is most likely caused by a structure unable to spawn properly due to hitting the world's min y or max y build thresholds or a broken RS datapack.
  Try teleporting to: class_2338{x=9861, y=92, z=-6344} and see if the structure generated fine with the required structure piece or if it is indeed missing it.
  Please report the issue to Repurposed Structures's dev with latest.log file if the structure is not cut off by world min/max y build thresholds.
