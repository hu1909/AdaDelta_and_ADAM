# An Analysis and Implementation of Adaptive Optimization Algorithms

This repository provides a research about several popular adaptive optimization algorithms used in training deep neural networks. It includes both a theoretical analysis within mathematic formula and practical Python implementations from scratch.

The primary goal is to explain the motivation behind adaptive methods, detail their mathematical foundations, and provide hands-on implementations to help understand how they work in practice.

---
## 📓 Notebooks

### 1. `ADADelta_vs_ADAM_Analysis.ipynb`
This is the main analytical notebook that ties everything together. It provides a comparison between the **ADADelta** and **ADAM** optimizers.

**Key Content:**
* **The Need for Adaptive Optimization**: Discusses the limitations of traditional methods.
* **Prerequisites**: Detailed explanations and implementations of **AdaGrad** and **Exponential Moving Average (EMA)**, which are foundational to understanding ADADelta and ADAM.
* **ADADelta and ADAM**: A side-by-side analysis of their core mechanics, mathematical formulas, and the motivation behind their designs.
* **Limitations and Improvements**: Explores the practical failure modes of ADAM and introduces the **Yogi** improvement to address variance issues.
* **Comparative Analysis and Recommendations**: A summary table comparing ADADelta and ADAM, with concluding recommendations for their use.
* **Practical Applications**: Discusses use cases in NLP and Computer Vision and provides practical exercises for implementation.

---
### 2. Implementation Notebooks
These notebooks contain standalone Python implementations of each algorithm, complete with simple test cases to demonstrate their functionality.

* **`AdaGrad-implementation.ipynb`**: Implements the AdaGrad algorithm, which adapts the learning rate for each parameter based on historical gradients. It is particularly effective for sparse features.

* **`AdaDelta-implementation.ipynb`**: Provides an implementation of AdaDelta, an improvement on AdaGrad that mitigates its aggressively decaying learning rate by using a limited window of past gradients.

* **`Adam-implementation.ipynb`**: Implements the ADAM (Adaptive Moment Estimation) optimizer. This notebook includes the standard ADAM algorithm as well as the **Yogi** improvement, which helps control the second-moment estimate for more stable training.

* **`EMA_class.py`**: A class for Exponential Moving Average (EMA). EMA is a key statistical method used in optimizers like ADAM to smooth out gradient updates by giving more weight to recent data points.

---
## ✨ Covered Algorithms
* **Stochastic Gradient Descent (SGD)** (as a baseline)
* **AdaGrad**
* **Exponential Moving Average (EMA)**
* **AdaDelta**
* **ADAM**
* **Yogi** (as an improvement to ADAM)
