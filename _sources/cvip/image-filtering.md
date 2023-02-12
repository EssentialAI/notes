# Image Filtering

Image filtering is working on the 2D image (after capturing). Filtering is very close to Convolution.

Image filtering is used to:
* Enhance images
  * Denoise, resize, increase contrast etc.
* Extract information from images
  * Textures, edges, distinctive points
* Detect patterns
  * Template matching

When we apply a filter of size $c \times c$ on an image of $n \times n$ dimensiions, the resultant image (without image padding) is $(n-c+1) \times (n-c+1)$

Convolution is a summation of element-wise multiplication of pixel intensities in an image region with the image filter that is applied.

In math terms,

$$
h[m,n] = \sum_{k,l}g[k,l] f[m+k, n+l]
$$

Image filtering             |  Image filtering |  
:-------------------------:|:-------------------------:
![](/imgs/img-filtering1.PNG)  |  ![](/imgs/img-filtering3.PNG)

**Image filtering with the above kernel achieves the smoothining effect. (removes sharp features).

## Convolution

```{figure} /imgs/convolution.PNG

---
height: 150px
name: convolution
---

Convolution
```

```{admonition} Why to flip the kernel?
:class: tip

To preserve commutative and associative properties of the convolution operation.
```

The convolution step measures how close the vectors are in terms of the angle between the vectors.

Convolution is very close to correlation, but we first flip the kernel vertically and horizontally and then compute the dot product to get each pixel of the output image.

```{seealso}
Visual representation of $3 \times 3$ convolution filters is shown [here](https://medium.com/@icecreamlabs/3x3-convolution-filters-a-popular-choice-75ab1c8b4da8) and this git [repo](https://github.com/vdumoulin/conv_arithmetic/blob/master/README.md)

Visual examples for image filtering are shown [here](https://www.codingame.com/playgrounds/2524/basic-image-manipulation/filtering)

Information about strided convolution and non-strided convolution here given [here](https://stats.stackexchange.com/questions/360899/difference-between-strided-and-non-strided-convolution)
```
## Image shift using convolution


```{figure} /imgs/shift-convolution.PNG

---
height: 150px
name: shift-convolution
---

Shift using convolution
```

Image Sharpening             |  Image Sharpening   
:-------------------------:|:-------------------------:
![](/imgs/sharpening-1.PNG)  |  ![](/imgs/sharpening-2.PNG)

## Edge detection

Sobel filter             | Sobel filter   
:-------------------------:|:-------------------------:
![](/imgs/sobel-edges.PNG)  |  ![](/imgs/sobel-edges-1.PNG)






