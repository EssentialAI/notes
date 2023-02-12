# Introduction and the Pinhole camera

Have you ever wondered what complex mathematics runs behind the miniature camera that we use in our every day life. Point and shoot cameras are ubiquotous to a point that we take camera technology for granted.

Consider an image of a railway track. 

```{image} /imgs/railway.jpg
:alt: railways
:class: bg-primary mb-1
:align: center
```

The rails look as if they converge at the end, however, we know that they do not. The depth of the scene is lost in the image (as the picture is a 2D image). The imperative question arises <span class = 'high'>How do we map a 3D object onto a 2D image?</span> Better yet, How to map a 3D point in space on a 2D plane? While making this 3D to 2D mapping, what is the information about the scene that is lost? What illusions would arise?

This section aims at answering the above questions while providing a detailed explanation of the pinhole camera.

**Computer Vision Overview**
1. Low-level vision
   1. Image processing
   2. Edge detection
   3. Feature detection
   4. Cameras
   5. Image formation
2. Geometry and algorithms
   1. Projective Geometry
   2. Stereo Vision
   3. Structure from motion
3. Recognition
   1. Face detection/recognition
   2. Category recognition
   3. Image segmentation

To model a camera, one must make sure to preserve both geometry and semantics of the scene. Some applications of computer vision include but not limited to [Single View modelling](https://www.semanticscholar.org/paper/Single-view-modeling-of-free-form-scenes-Zhang-Dugas-Phocion/0193a8ca0dc5c34cb81cccb8070666d6275738c7), Detection and Recognition, [Visual Question and Answering](https://www.sciencedirect.com/science/article/pii/S1077314217301170), Optical Character Recognition, Entertainment (e.g., Snapchat), Shape Reconstruction using depth sensors, [Building rome in a day!](https://grail.cs.washington.edu/rome/), 3D Scanning, Medical Imaging and so on.

# Image Formation

How a colorful image is formed? All the images are a resultant of the following entities:
1. Lighting Conditions
2. Scene Geometry
3. Surface Properties
4. Camera Properties

<span class = 'high'>The focus of this course is predominantly on the Camera Properties.</span> The image formation requires a light source (e.g., sun) continuously emits photons. These photons are reflected by the surface and a portion of this light is directed towards the camera.

**The sensor plane (the film) has physical existence, but the image plane is virtual.** The image plane is flipped upside down as compared to the sensor plane.

# Pinhole camera model

The pinhole camera makes sure that every unique point in the physical space falls on the film.

```{figure} /imgs/pinhole_1.PNG

---
height: 150px
name: pinhole_1
---

Pinhole camera
```

```{figure} /imgs/pinhole_2.PNG

---
height: 150px
name: pinhole_2
---

Pinhole camera Model
```

The image that we see on the screen after taking an image is virtual image plane. Same phenomenon happens in human eyes.

Zooming in and Zooming out changes the focal length of a camera. (Not digital zoom, optical zoom)

```{figure} /imgs/focal_length.PNG

---
height: 150px
name: focal length
---

Pinhole camera 2D representation
```
The above diagram gives us the first equation for image formation in computer vision. Given a 3D point $P =(X,Y,Z)^T$, the camera projects this point to onto a $2D$ image plane to $p = (x,y)^T$. From the above figure:

\begin{gather*}
\frac{\text{Object size}}{\text{Object distance}} = \frac{\text{Image size}}{\text{Focal Length}}
\end{gather*}

```{math}
:label: first_equation
\frac{X}{Z} = \frac{x}{f}, \frac{Y}{Z} = \frac{y}{f}
```

$$x=f \frac{X}{Z}, y = f\frac{Y}{Z}$$

This is the simplest form of perspective projection. You can change the size of the image by changing any of the above 3 parameters. For a simple example of human face, the image size can be increased by i) actually having a bigger object size $Y$, ii) increasing the focal length $f$, and iii) bringing the object closer to the camera (decreasing $Z$)

In the above figure the focal length is the only parameter that can be changed (as the size of the object and the distance from camera is assumed to be fixed.) This means that upon increasing the focal length the size of the image increases proportionally. When we zoom in, we increase the focal length.


```{admonition} If I zoom in/out of a picture after taking a picture, will focal length change?
:class: tip
After taking a picture, if you zoom in and zoom out, it is a digital zoom. It does not change the focal length of the camera.
```

```{admonition} How to calculate the default focal length of a smartphone camera?
:class: tip
[Calculating the focal length of camera](https://aapt.scitation.org/na101/home/literatum/publisher/aip/journals/content/pte/2019/pte.2019.57.issue-1/1.5084932/20181219/1.5084932.fp.png_v03)
```

**The aim of a camera is to map each of the 3D point in the 3D world to a location in the 2D image plane. Camera does the 3D-2D mapping.** It is also called as the Perspective projection. This leads to a question about how to recover a 3D location of a point from a 2D image.

While projecting from 3D to 2D, the depth information is lost (also the angles between objects in 3D) are lost. <span class = 'high'>Each ray becomes a pixel on the image plane.</span>

```{note}
In the above perspective projection, the angle between lines is not preserved and the depth information is lost.
```

When the distance between camera and the object is too large (god’s view), the difference in sizes of closer objects and far objects is not preserved.

$x = sX, y = sY, \text{ where } s=\frac{f}{Z_0}$, $Z_0$ is the distance between camera and the object.

## Projection Matrix and the Intrinsic parameters
```{math}
:label: second_eq
Z \begin{pmatrix}
\frac{fX}{Z} \\
\frac{fY}{Z} \\
1
\end{pmatrix}
=
\begin{pmatrix}
fX \\
fY \\
Z
\end{pmatrix} = \begin{bmatrix}
f & 0 & 0 & 0\\
0 & f & 0  & 0\\
0 & 0 & 1 & 0
\end{bmatrix}\begin{pmatrix}
X\\
Y\\
Z\\
1
\end{pmatrix}
```

The simplest form of perspective projection in matrix form is given by the above equation.

```{admonition} What is the need for extra row in the 3D coordinate?
:class: tip

The extra column of zeros and the extra 1 in the 3D coordinate is added to incorporate the translation.
```

```{admonition} What do the distances $X, Y, Z$ mean here?
:class: note
$X,Y,Z$ are the relative coordinates of a 3D point from the camera origin. This means that when the object is moved or the camera is moved, the values of $X,Y,Z$ change.
```
This leads us to the question, What about the values of $x,y$? These pixel values are relative to the origin `Principal point` of the image plane. Typically the origin of an image is located at the bottom left or the top left.

Hence, there is a need to make sure the principal point overlaps with the image origin, and we add an **offset** $o_x$ and $o_y$ within the image plane to resolve this issue. **Keep in mind that this offset is not caused by the movement of the object or the camera. It an intrinsic parameter of every camera.**

The {eq}`second_eq` becomes:

```{math}
:label: third_eq

\begin{pmatrix}
fX + Zo_x \\
fY + Zo_y\\
Z
\end{pmatrix} = \begin{bmatrix}
f & 0 & o_x & 0\\
0 & f & o_y  & 0\\
0 & 0 & 1 & 0
\end{bmatrix}\begin{pmatrix}
X\\
Y\\
Z\\
1
\end{pmatrix}
```
$$
K = \begin{bmatrix}
f & 0 & o_x \\
0 & f & o_y  \\
0 & 0 & 1 
\end{bmatrix}
$$

The focal length $f$ need not be same along the $x$ and $y$ axes always. A general form of the projection matrix is:

```{math}
:label: projection_matrix
K = \begin{bmatrix}
f_x & 0 & o_x \\
0 & f_y & o_y  \\
0 & 0 & 1 
\end{bmatrix}
```

**This is the (Intrinsic) calibration matrix.**

There is an advanced version of the above matrix. It is called Camera Calibration matrix.

```{math}
:label: intrinsic_eq
K = \begin{bmatrix}
\gamma f_x & s & o_x \\
0 & f_y & o_y  \\
0 & 0 & 1 
\end{bmatrix}
```

$\gamma$ - when you zoom in and zoom out, the $x$ and $y$ co-ordinates are changed proportionally. However if there is an unproportional change in $x$ and $y$ axes, $\gamma$ takes care of that. $\gamma$ is also called the `aspect ratio` of the pixel.

$s$ - skew of the sensor pixel, i.e., if the pixel is a parallelogram and not a square.

**There are 5 intrinsic parameters for a camera.** Refer {eq}`intrinsic_eq`

## Extrinsic parameters of a camera
The extrinsic parameters come into picture, even before shooting an image. Where the camera is located and it's angle. **(Rotation and Translation)**.

These are the parameters that identify uniquely the transformation between the <span class = 'high'>unknown camera reference frame</span> and the <span class='high'>known world reference frame.</span>

Determining these parameters includes:
1. Finding the translation vector between the relative positions of the origins of the two reference frames.
2. Finding the rotation matrix that brings the corresponding axes of the two frames into alignment (i.e., onto each other).

```{figure} /imgs/rot_translate.PNG

---
height: 150px
name: rot_translate
---

Rotation and Translation from world coordinates to camera coordinates.
```

Using the extrinsic camera parameters, we can find the relation between the coordinates of a point $P$ in the world $(P_w)$ and camera $(P_c)$ coordinates:

```{math}
:label: extrinsic

P_c = R(P_w-T)

```
where

```{math}
:label: extrinsic 1
R = \begin{bmatrix}
r_{11} & r_{12} & r_{13}  \\
r_{21} & r_{22} & r_{23}   \\
r_{31} & r_{32} & r_{33} 
\end{bmatrix}
```

$$ \text{If } P_c =  \begin{bmatrix}
X_c \\
Y_c \\
Z_c 
\end{bmatrix} \text{ and } P_w = \begin{bmatrix}
X_w \\
Y_w \\
Z_w 
\end{bmatrix}, \text{ then}
$$

```{math}
:label: extrinsic_final

\begin{bmatrix}
X_c \\
Y_c \\
Z_c 
\end{bmatrix} = \begin{bmatrix}
r_{11} & r_{12} & r_{13}  \\
r_{21} & r_{22} & r_{23}   \\
r_{31} & r_{32} & r_{33} 
\end{bmatrix}\begin{bmatrix}
X_w-T_x \\
Y_w-T_y \\
Z_w-T_z 
\end{bmatrix}
```
In other words, we first translate the coordinates to match the camera coordinates and then rotate the axes so that both camera axes and world coordinate axes overlap.

$$
X_c = R_1^T(P_w-T) \\
Y_c = R_2^T(P_w-T) \\
Z_c = R_3^T(P_w-T)
$$

where $R_i^T$ corresponds to the $i^{th}$ row of the rotation matrix.

```{admonition} What is a camera?
:class: tip

Camera is nothing but a 3D point to 2D point mapping function that has 11 parameters (intrinsic and extrinsic).
```

## 3D to 2D mapping (both intrinsic and extrinsic)

1. Given an image of an object, we would like to find the intrinsic and extrinsic parameters of a camera.
2. With these intrinsic and extrinsic parameters, we want to use the camera to map any 3D point in the real world to a 2D coordinate on the image plane.

$[X_w, Y_w, Z_w]^T \rightarrow [X_c, Y_c, Z_c]^T$ is rigid transformation and $[X_c, Y_c, Z_c]^T \rightarrow s[x,y,1]$ is projective transformation (perspective projection).

$$
s\begin{bmatrix}x\\
y\\
1
\end{bmatrix} = \begin{bmatrix}
\gamma f_x & s & o_x \\
0 & f_y & o_y  \\
0 & 0 & 1 
\end{bmatrix} \begin{bmatrix} 1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
0 & 0& 1& 0\end{bmatrix} \begin{bmatrix}R_{3 \times 3} & 0_{3 \times 1} \\
0_{1 \times 3} & 1\end{bmatrix} \begin{bmatrix} I_{3 \times 3} & T_{3 \times 1} \\
0_{1 \times 3} & 1\end{bmatrix}\begin{bmatrix} X_w \\
Y_w \\
Z_w \\
1\end{bmatrix}
$$

```{math}
:label: projection

s\begin{bmatrix}x\\
y\\
1
\end{bmatrix} = \begin{bmatrix}
f_x & 0 & o_x \\
0 & f_y & o_y  \\
0 & 0 & 1 
\end{bmatrix} \begin{bmatrix}
r_{11} & r_{12} & r_{13} & T_x \\
r_{21} & r_{22} & r_{23} & T_y  \\
r_{31} & r_{32} & r_{33} & T_z
\end{bmatrix} \begin{bmatrix} X_w \\
Y_w \\
Z_w \\
1\end{bmatrix}
```

$[x, y]^T$ are the image coordinates and $[X_w, Y_w, Z_w]^T$ are the world coordinates. $T_{3 \times 1} = [T_x, T_y, T_z]^T$ is the translation vector.

The intrinsic and extrinsic parameters combine to form the matrix $M$.

$$
M = M_{in}.M_{ex} = \begin{bmatrix}m_{11} & m_{12} & m_{13} & m_{14}  \\
m_{21} & m_{22} & m_{23} & m_{24}  \\
m_{31} & m_{32} & m_{33} & m_{34} \end{bmatrix}
$$

#### Intuition behind the 3D $\rightarrow$ 2D mapping in a camera.

```{math}
:label: mapping_matrix

s\begin{bmatrix}x\\
y\\
1
\end{bmatrix} = \begin{bmatrix}m_{11} & m_{12} & m_{13} & m_{14}  \\
m_{21} & m_{22} & m_{23} & m_{24}  \\
m_{31} & m_{32} & m_{33} & m_{34}\end{bmatrix} \cdot \begin{bmatrix} X_w \\
Y_w \\
Z_w \\
1\end{bmatrix}
```

Let's suppose, you have $n$ image coordinates of a camera and their corresponding world coordinates. Our aim to find the matrix $M$. <span class = 'high'>From {eq}`mapping_matrix`, we have:</span>

$$
sx = m_{11}X_w + m_{12}Y_w + m_{13}Z_w + m_{14} \\
sy = m_{21}X_w + m_{22}Y_w + m_{23}Z_w + m_{24} \\
s = m_{31}X_w + m_{32}Y_w + m_{33}Z_w + m_{34}$$

To solve for the matrix $M$,

```{figure} /imgs/matrix_m.PNG

---
height: 150px
name: matrix_m
---

Solving for the matrix $M$
```
where the first matrix is of size $2n \times 12$ ($n$ is the number of available points.)

In the above homogeneous linear equation $Ax=0$, we know the values of image coordinates and the real-world coordinates. We are required for find the elements of the matrix $M$. The above equation has infinite solutions for $Ax = 0$, since we can randomly scale $x$ with a scalar $\lambda$ such that $A(\lambda x)= 0$. Therefore, we assume $||x||=1$, solving the equation can be converted to:

$$
min||Ax||
$$

The minimization problem can be solved with <span class = "high">Singular Value Decomposition (SVD)</span>. Assume that $A$ can be decomposed to $U\Sigma V^T$, we have

$$
min||Ax|| = ||U \Sigma V^Tx|| = ||\Sigma V^Tx||
$$

Since $||V^Tx||=||x||=1$, then we have $min||Ax|| = ||\Sigma y||$.

As $||y||=1$, $x$ should be the last row of $V^T$.

Once we have the matrix $M$, 

```{math}
:label: m_matrix
M = \begin{bmatrix}m_{11} & m_{12} & m_{13} & m_{14}  \\
m_{21} & m_{22} & m_{23} & m_{24}  \\
m_{31} & m_{32} & m_{33} & m_{34}\end{bmatrix} = \begin{bmatrix} f_xr_{11}+o_xr_{31} & f_x r_{12}+o_xr_{32} & f_xr_{13}+o_xr_{33}&f_xT_x+o_xT_z \\
f_y r_{21}+o_yr_{31} & f_yr_{22}+ o_y r_{32} & f_yr_{23}+o_yr_{33} & f_yT_y+o_yT_z \\
r_{31} & r_{32} & r_{33} & T_z\end{bmatrix}
```

Here, $M$ is the projection matrix. Let's define 

$$
\begin{align}
m_1 &= (m_{11}, m_{12}, m_{13})^T \\ 
m_2 &= (m_{21}, m_{22}, m_{23})^T \\
m_3 &= (m_{31}, m_{32}, m_{33})^T \\
m_4 &= (m_{14}, m_{24}, m_{34})^T
\end{align}
$$

Also we define,

$$
\begin{align}
r_1 &= (r_{11}, r_{12}, r_{13})^T \\
r_2 &= (r_{21}, r_{22}, r_{23})^T \\
r_3 &= (r_{31}, r_{32}, r_{33})^T
\end{align}
$$

Observe that $(r_1, r_2, r_3)$ is the rotation matrix, then

```{math}
:label: rotation_m

(r_1, r_2, r_3) \begin{pmatrix}
r_1^T\\
r_2^T\\
r_3^T 
\end{pmatrix} = \begin{pmatrix}
1 & 0 & 0\\ 
0 & 1 & 0\\ 
0 & 0 & 1
\end{pmatrix}
```

Then we have $r_i^Tr_i = 1, r_i^Tr_j=0 \enspace (i \neq j)$.

From $M$ we have,

$$
m_1^Tm_3 = o_x $$

$$m_1^Tm_1 = f_x^2+o_x^2$$

$$o_x = m_1^Tm_3, \enspace o_y = m_2^Tm_3$$

$$f_x = \sqrt{m_1^Tm_1 - o_x^2}, \enspace f_y = \sqrt{m_2^Tm_2 - o_y^2}$$

# Summary
This chapter discusses about the pinhole camera model. The intrinsic and extrinsic camera paramters. Given a 3D world coordinates of an object, a camera performs a 3D $\rightarrow$ 2D mapping of the point onto an image plane. There are a total of 11 paramters for any camera to perform this perspective projection mapping.

This chapter also explains the mathematics used to find the intrinsic and extrinsic parameters of a camera using image coordinates and world coordinates. Given an image of an object, and $n$ world coordinates and image coordinates, we discuss the mathematics to find the matrix $M = M_{in}\cdot M_{ex}$ that would help us map any 3D point in real world to a 2D point on image plane.

The next chapter provides the code for the above mathematics. We use chessboard corners as objects and try to find the intrinsic and extrinsic parameters of a given camera.

<!-- ### Rotation matrix explained -->
















