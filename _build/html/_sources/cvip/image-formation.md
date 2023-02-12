# Image Formation and Stereo Vision

Ideally we would like to collect more light for the camera. For this reason, we add lens to the camera. The issue by adding a lens to the camera is that, lens has its own focal point.

With lens, there arise some issues like chromatic aberration. This is a non-trivial issue.

## Depth of Field

Depth of Field (DOF) is the region in the 3D world where you can clearly see the object. It is also defined as the distance between nearest and farthest objects that are in acceptably sharp focus in an image.

Aperture can be used to change the depth of field. Smaller the aperture, bigger the depth of field.

```{figure} /imgs/dof.PNG

---
height: 150px
name: dof
---

Changing DOF using aperture
```

```{figure} /imgs/dof1.PNG

---
height: 150px
name: dof1
---

Changing DOF using aperture
```


```{figure} /imgs/exposure_triangle.PNG

---
height: 150px
name: exposure_triangle
---

Exposure Triangle
```

Aperture, shutter speed and ISO are neither intrinsic nor extrinsic parameters.

Field of view is another parameter that is dependent on the screen resolution.

```{figure} /imgs/fov.PNG

---
height: 150px
name: fov
---

Field of view
```

Size of field of view governed by size of the camera retina.

$$
\phi = tan^{-1}(\frac{d}{2f})
$$

Smaller FOV = larger the focal length.

So far we have talked about the geometry of the camera, now we shall discuss about the color of the image.

## Photometric Imaging

* Illuminating and light sources
* Surfaces and reflection
* Camera response

```{admonition} A note on Sensor types used today:
:class: tip

> CCD (charge-coupled device)
* Most common, high sensitivity, high power. (Some mobile phones use CCD).
> CMOS
* Simple to fabricate, lower sensitivity, lower power. (Surveillance cameras use CMOS).
```

# Stereo Vision and Multiple View Geometry

Until this section, the main focus of the course is finding the intrinsic and extrinsic parameters of a camera. For 3D $\rightarrow$ 2D mapping, we have 11 paramters.

This section talks about the 2D $\rightarrow$ 3D mapping. Given an image coordinate, can we approximate the 3D location of the object. This is an ill-posed problem.

<span class ='high'>Although, we cannot solve the 2D $\rightarrow$ 3D mapping using one image, we can solve the problem using 2 images.</span> This the reason humans can perform the depth approximation and image processing better using 2 eyes.

This problem is called stereo vision. The main aim of using stereo vision is to perceive the depth $Z$.

**Visual Cues for 3D**
* Shading
* Texture
* Focus
* Motion
* Highlights
* Shadows
* --

## Triangulation

Stereo vision determines the position of a point in space by finding the intersection of the two lines passing through the centre of projection and projection of object point on image planes.

```{figure} /imgs/stereo1.PNG

---
height: 150px
name: triangulation
---

Triangulation
```

## Core problems in stereo

* **Correspondence**:
Given a point in one image, how can I find the corresponding point 'x' in another one?
* **Camera geometry**:
Given corresponding points in two images, find camera matrices, position and pose.
* **Scene geometry**:
Find coordinates of 3D point from its projection into 2 or multiple images.

### Disparity

Disparity is defined as the difference in the location of a feature point between the right and left images. <span class = 'high'>Disparity is high for closer objects and low for distant objects.</span>

```{figure} /imgs/disparity.PNG

---
height: 150px
name: disparity
---

Disparity
```

disparity $d = x^l-x^r$.

$x^l$ is the pixel location in the left image.
$x^r$ is the pixel location in the right image.

**Depth from disparity**

```{figure} /imgs/depth_from_disparity.PNG

---
height: 150px
name: depth_from_disparity
---

Depth from Disparity
```
B - Baseline,
Z - Depth,
d - Disparity,
f - focal length

Among B,f,Z,d, disparity has the most uncertainty.

_Keep in mind that the image plane considered here is the virtual image plane._

Another point to note that disparity calculation after the camera are calibrated and both the image planes are along the same line. To achieve this, we perform image rectification and image plane alignment.

Once the correspondence problem is solved, we can calculate the depth at every point in the image.

### Epipolar Geometry

```{figure} /imgs/epipolar_geometry.PNG

---
height: 150px
name: epipolar_geometry
---

Epipolar Geometry
```

* **Baseline** - Line joining the camera centers.
* **Epipole** - Point of intersection of baseline with the image plane.
* **Epipolar plane** - Plane containing baseline and world point.
* **Epipolar line** - Intersection of epipolar plane with the image plane.

* All epipolar lines intersect at the epipole.

Let us consider an example where the cameras are not aligned and are required to be recitified.

```{figure} /imgs/epipolar_1.PNG

---
height: 150px
name: epipolar_1
---

Cameras not aligned
```

Once the images are aligned, the epiholes are at infinity.

```{figure} /imgs/epiholes.PNG

---
height: 150px
name: epiholes
---

Epiholes when cameras are aligned.
```

### Image Rectification
This process is the correction of cameras so that cameras (image planes of cameras) are parallel to the baselines.

_This is done when the two cameras do not have the same focal lengths or are not parallel to the baseline._

**Image Rectification is a projective transformation.**

```{figure} /imgs/rectification.PNG

---
height: 150px
name: rectification
---

Image Rectification example.
```

Advantage of image rectification is that the search for a corresponding pixel from left and right image becomes a <span class = 'high'>linear search</span>. You only need to search for the pixel along the epipolar line that is already rectified.

This leads to the correspondence problem that we want to solve to begin with.

### Basic Stereo matching algorithm

As the images are rectified, we can perform a linear search algorithm to find the corresponding pixel from left image to right image.

This leads us to the correspondence problem. How to find the matching pixel along the line?

<span class = 'high'>Usually, we use an image patch or a window.</span>

We use either Sum of Squared Distance or the Normalized correlation to find the matching patch between two images.

You calculate SSD or NCC for every pixel. <span class = 'high'>The lower the SSD, the better. The higher the value of NCC, the better the match.</span>

The size of the window is a hyperparameter to be tuned. If the window size is large - there will be a smooth disparity map, and low details.

The window searching method fails if the selected pixel for searching is generic, or noise.

```{figure} /imgs/sim_failure.PNG

---
height: 150px
name: sim_failure
---

Window based similarity search failure.
```

Closer objects have more disparity.

$$
\text{Length of Baseline} \propto \frac{1}{\text{depth error}}
$$

Constraints with window based search:
* Uniqueness constriaint
* Ordering constraint
* Smoothness constraint (neighboring pixels are similar (expect at edges))












