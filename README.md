---

# **Minor_ArtiFuse_GAN_Training**  
### **Facial Image Inpainting with Pix2Pix cGAN**  

ArtiFuse presents an innovative approach to **facial image inpainting** using a specialized **Conditional Generative Adversarial Network (cGAN)**. This project explores **GAN architectures** for intelligent **facial restoration**, allowing users to seamlessly reconstruct masked regions in images.  

While **state-of-the-art models** exist, this project focuses on experimentation and pushing the limits of **GAN-based inpainting** within constrained computational resources. The ultimate goal is to provide a practical **toolset** for facial inpainting tasks and create a **user-friendly web application** for image input, mask creation, and restoration.  

---

## 🚀 **Project Overview**  

This repository contains the **code** required to **train, retrain, and test** the Pix2Pix cGAN model for facial inpainting. The model is trained on the **CelebA dataset** using **roughly 24,000 images** iteratively.  


### 🔹 **Key Features**  
✔️ **Image Preprocessing**: Prepares CelebA images for training.  
✔️ **GAN Training**: Implements Pix2Pix cGAN to train the model.  
✔️ **Model Retraining**: Allows saved models to be retrained with new data.  
✔️ **Performance Testing**: Evaluates the model’s output on test data.  
✔️ **Mask Generation**: Generates masked images for training.  

---

## 📁 **Repository Structure**  

| File | Description |
|------|------------|
| `image_preprocessing_training.ipynb` | Loads the uploaded images from named directories in google drive and trains the models|
| `loading_the_trained_model_and_retraining.ipynb` | Allows retraining of an existing saved model. |
| `testing_model_performance_on_data.ipynb` | Evaluates the trained model on test images. |
| `masking_generation.py` | Adds masks to CelebA images for inpainting training. |

---



**Features:**  
✔️ **Upload & preprocess images**  
✔️ **Create and modify masks for inpainting**  
✔️ **Apply the trained GAN model for image restoration**  
✔️ **Download the inpainted output**  

---

### 📊**Performance after 26 epochs on 8000 dataset (~8 epochs on total 24000 dataset iteratively)**  
### **Performance on Testing Dataset**  
![Performance on Testing Dataset](https://github.com/user-attachments/assets/85121057-3ded-4500-844b-d35f456c529d)  

## **Training Loss Curve**  
### **initial loss**
![Image](https://github.com/user-attachments/assets/2c761e39-a54c-42c1-ad8e-b01c5595c048)
![Image](https://github.com/user-attachments/assets/3fd5c647-2496-4b5d-8617-ee15505a4da4)
### **final loss**
![Loss Graph 1](https://github.com/user-attachments/assets/f7806650-4bbf-4c10-af5c-aed30042ceaf)  
![Loss Graph 2](https://github.com/user-attachments/assets/88818f59-6e04-44a5-b734-9c5b638e5c14)  

---

## 🖼️ **Sample Outputs**  
![Output Sample 1](https://github.com/user-attachments/assets/7b9ed505-1405-4754-a29b-5babeaa3fa62)  
![Output Sample 2](https://github.com/user-attachments/assets/513734c1-0079-4450-b3ed-a9040f56c634)  
![Output Sample 3](https://github.com/user-attachments/assets/8ba17259-55d8-419f-9e07-453f14af0275)  
![Image](https://github.com/user-attachments/assets/53a3090e-9b74-41e7-8ec9-c3c3bb8510d9)
![Image](https://github.com/user-attachments/assets/4d542adf-5553-4d96-8bf2-3f706bc6d182)
![Image](https://github.com/user-attachments/assets/cef4eeee-c8fc-4116-8508-b68a8a7ef3d6)


---


## 🌐 **Web Implementation**  

🔗 **Web Application Repository(not deployed)**:  
[**Minor_ArtiFuse Web Application**](https://github.com/SauravKumarMahato/Minor_ArtiFuse.git)  

## **Frontend Preview**  
![Website Frontend](https://github.com/user-attachments/assets/e754922a-d293-4ed2-978b-ddcf4bd42401)  


## 🔍 **Project Context & Motivation**  

The **ArtiFuse GAN model** is designed to intelligently reconstruct missing regions in facial images. It can:  
✔️ **Erase imperfections** such as blemishes, scars, and wrinkles.  
✔️ **Restore old or damaged photographs** with missing sections.  
✔️ **Enable facial editing** by removing unwanted elements from images.  

Despite the existence of **highly advanced models**, this project focuses on **researching and testing** the capabilities of **GAN architectures** within limited computational constraints.  

## 🛠 **Future Work**  
- ✅ **Enhance training with more diverse datasets**  
- ✅ **Improve inpainting results for extreme occlusions**  
- ✅ **Deploy a web-based interactive application**  

---

## 📌 **Keywords**  
**GAN, Pix2Pix, cGAN, image inpainting, facial inpainting, AI restoration, deep learning, image reconstruction, AI-generated content.**  

---

