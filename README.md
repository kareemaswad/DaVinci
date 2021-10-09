# Pick and Place


First, make sure you get the most recent transformations
```python 
update_transforms()
```

Second, define objects
```python
balls, bowls = images_to_object_positions(left_image, right_image)
```

Third, find the objects coordinates with respect to all frames
```python
world_position_to_joints(balls)
world_position_to_joints(bowls)
```

Call this to complete a pick a place demonstration using one PSM and one bowl 
```python
pick_and_place_one(balls, bowls[0], psm2)
```
Call this to complete a pick and place demonstration using two PSMs and two bowls
```python
pick_and_place_two(bowls, balls)
```

To move the camera in a way that centers the frame about an object, in this case the first ball detected
```python
center_frame(balls[0].world_coordinates, 0.005, 0.005)
```

