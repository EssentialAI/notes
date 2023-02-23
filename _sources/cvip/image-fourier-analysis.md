# Image Fourier Analysis

We use sine waves to perform image fourier analysis because any signal can be decomposed as a linear summation of sine waves with different amplitudes and time periods.

1D sine wave decomposition | sine wave decomposition
:-------------------------:|:-------------------------:
![](/imgs/sine-wave.PNG)   |  ![](/imgs/sine-wave2.PNG)


```{figure} /imgs/fourier-analysis.PNG

---
height: 150px
name: fourier-analysis
---

Fourier analysis for filters
```

Before performing the fourier analysis, images are subsampled. This is done to overcome the calculation head.

```{figure} /imgs/filter-pipeline.PNG

---
height: 150px
name: filter-pipeline
---

Pipeline
```

## Convolution represented in terms of Fourier Transforms

```{figure} /imgs/fourier-conv.PNG

---
height: 150px
name: fourier-conv
---

Convolution in terms of fourier
```


_ | _ 
:-------------------------:|:-------------------------:
![](/imgs/filter-spatial.PNG)  |  ![](/imgs/filter-freq.PNG)

```{note}
FFT is one of the most beautiful algorithms of all time. Learn the essence of FFT [here](https://www.youtube.com/watch?v=nmgFG7PUHfo) and [here](https://www.youtube.com/watch?v=h7apO7q16V0)
```

# Image Smoothing - Gaussian Kernel


```{figure} /imgs/guassian-kernel.PNG

---
height: 150px
name: gaussian-kernel
---

Gaussian Kernel
```

```{figure} /imgs/smoothing.PNG

---
height: 150px
name: smoothing
---

Image smoothing
```

```{figure} /imgs/low-pass-filter.PNG

---
height: 150px
name: low-pass-filter
---

Low-pass Filter
```

## Box v/s Gaussian filter

```{figure} /imgs/box-vs-gaussian.PNG

---
height: 150px
name: box-vs-gaussian
---

Box vs Gaussian filters
```

Box filter | Gaussian filter 
:-------------------------:|:-------------------------:
![](/imgs/box-fourier.PNG)  |  ![](/imgs/gaussian-fourier.PNG)

# Template Matching

We have the candidates for correspondence from the left image and the right image. How do we match the corresponding regions of the both images.

Template matching is one way to perform this correspondence check.

Ways to perform template matching:
* Correlation
* Zero-mean correlation
* Sum Square Difference
* Normalized Cross Correlation

SSD | NCC 
:-------------------------:|:-------------------------:
![](/imgs/ssd-1.PNG)  |  ![](/imgs/ncc-2.PNG)


```{figure} /imgs/ncc-1.PNG

---
height: 150px
name: ncc-1
---

Normalized Cross Correlation
```
SSD with dark patch | NCC with dark patch
:-------------------------:|:-------------------------:
![](/imgs/ssd-2.PNG)  |  ![](/imgs/ncc-3.PNG)

## SSD v/s NCC

* SSD is faster, but sensitive to overall intensity
* NCC is slower, but invariant to local average intensity and contrast.

```{note}
NCC captures the cosine of angle between the vectors. NCC is similar to cosine similarity with normalization.
```

## Image pyramids

Image pyramid is formed by applying gaussian filter on an image and then sampling every other pixel in the image.

Image Pyramid | Image Pyramid
:-------------------------:|:-------------------------:
![](/imgs/img-pyramid-1.PNG)  |  ![](/imgs/img-pyramid-2.PNG)

The extra image samples added to the image contribute to 1/3 of the original image.

## The essence of gaussian smoothing

Before Smoothing | After Smoothing | The contour
:-------------------------:|:-------------------------:|:-------------------------:
![](/imgs/before-smooth.PNG)  |  ![](/imgs/after-smooth.PNG) |  ![](/imgs/the-filter.PNG)

```{seealso}
More information about Gaussian kernels can be found [here](https://dsp.stackexchange.com/questions/3002/why-are-gaussian-filters-used-as-low-pass-filters-in-image-processing)
```

**Gaussian Pyramids and Laplacian Pyramids**

```{figure} /imgs/laplacian-pyramid.PNG

---
height: 150px
name: laplacian-pyramid
---

Laplacian Pyramid
```

## Finding edges using intensity values 

```{figure} /imgs/edges-fourier.PNG

---
height: 150px
name: edges-fourier
---

Edge detection in the 1D frequency domain.
```

The above figure is for the 1D case. An image is 2D, how to represent the edges in terms of gradients?

Edges as gradients | Edges as gradients
:-------------------------:|:-------------------------:
![](/imgs/image-gradient-1.PNG)  |  ![](/imgs/image-gradient-2.PNG)

$\theta$ represents the direction of the edge.

Edges for noisy input | Edges for noisy input
:-------------------------:|:-------------------------:
![](/imgs/edge-1.PNG)  |  ![](/imgs/edges-2.PNG)


