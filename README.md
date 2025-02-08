
---

# **ArtiFuse: Facial Image Inpainting with Pix2Pix cGAN**  

**Authors:**  
- Rajesh Adhikari  
- Sandhya Baral  
- Saurav Kumar Mahato  

ArtiFuse is a deep learning project that explores **facial image inpainting** using a **Conditional Generative Adversarial Network (cGAN)**. The goal is to intelligently reconstruct masked regions in images, enabling seamless facial restoration.  

While state-of-the-art models exist, this project focuses on **experimenting with GAN-based inpainting** under **limited computational resources**. The ultimate aim is to develop a **practical toolset** and a **user-friendly web application** for facial inpainting.  

---  

## 🚀 **Project Overview**  

This repository contains the complete **training, retraining, and testing pipeline** for the Pix2Pix cGAN model, trained at **128×128 resolution** (scalable for higher resolutions but limited by compute). The model is trained on the **CelebA dataset** using approximately **24,000 images iteratively**.  

### 🔹 **Key Features**  
✔️ **Image Preprocessing** – Prepares CelebA images for training.  
✔️ **GAN Training** – Implements the Pix2Pix cGAN model.  
✔️ **Model Retraining** – Supports fine-tuning with new data.  
✔️ **Performance Evaluation** – Tests the model’s inpainting accuracy.  
✔️ **Mask Generation** – Automates mask creation for training.  

---  

## 📁 **Repository Structure**  

| File | Description |
|------|------------|
| `image_preprocessing_training.ipynb` | Preprocesses images and trains the model using Google Drive storage. |
| `loading_the_trained_model_and_retraining.ipynb` | Loads and fine-tunes an existing trained model. |
| `testing_model_performance_on_data.ipynb` | Evaluates the trained model on test images. |
| `masking_generation.py` | Generates masked images for inpainting training. |

---  

## 🎯 **Model Performance**  

### 📊 **Training Progress (After 26 epochs on 8,000 images, ~8 epochs on 24,000 images iteratively)**  

#### **Testing Dataset Results**  
![Performance on Testing Dataset](https://github.com/user-attachments/assets/85121057-3ded-4500-844b-d35f456c529d)  

#### **Training Loss Curve**  

**Initial Loss:**  
![Image](https://github.com/user-attachments/assets/2c761e39-a54c-42c1-ad8e-b01c5595c048)  
![Image](https://github.com/user-attachments/assets/3fd5c647-2496-4b5d-8617-ee15505a4da4)  

**Final Loss:**  
![Loss Graph 1](https://github.com/user-attachments/assets/f7806650-4bbf-4c10-af5c-aed30042ceaf)  
![Loss Graph 2](https://github.com/user-attachments/assets/88818f59-6e04-44a5-b734-9c5b638e5c14)  

---  

## 🖼️ **Sample Outputs**  

| Input | Output |
|------|------|
| ![Output Sample 1](https://github.com/user-attachments/assets/7b9ed505-1405-4754-a29b-5babeaa3fa62) | ![Output Sample 2](https://github.com/user-attachments/assets/513734c1-0079-4450-b3ed-a9040f56c634) |
| ![Output Sample 3](https://github.com/user-attachments/assets/8ba17259-55d8-419f-9e07-453f14af0275) | ![Image](https://github.com/user-attachments/assets/53a3090e-9b74-41e7-8ec9-c3c3bb8510d9) |
| ![Image](https://github.com/user-attachments/assets/4d542adf-5553-4d96-8bf2-3f706bc6d182) | ![Image](https://github.com/user-attachments/assets/cef4eeee-c8fc-4116-8508-b68a8a7ef3d6) |

---  

## 🔗 **Pretrained Models (Generator & Discriminator)**  

The trained models are available on Google Drive:  
[**Download Models Here**](https://drive.google.com/drive/folders/1WsPnQztd-It34YWdiGAIMEihXENYfQ3T?usp=sharing)  

---  

## 🌐 **Web Implementation**  

🔗 **Web Application Repository (Not Deployed Yet):**  
[**Minor_ArtiFuse Web Application**](https://github.com/SauravKumarMahato/Minor_ArtiFuse.git)  

### **Frontend Preview**  
![Website Frontend](https://github.com/user-attachments/assets/e754922a-d293-4ed2-978b-ddcf4bd42401)  

---  

## 🔍 **Project Motivation & Applications**  

ArtiFuse is designed to intelligently reconstruct missing regions in facial images. Potential applications include:  
✔️ **Removing imperfections** (e.g., blemishes, scars, and wrinkles).  
✔️ **Restoring old or damaged photographs** with missing sections.  
✔️ **Facial editing** by removing unwanted elements.  

This project serves as an **experimental research tool**, exploring the limits of **GAN-based inpainting** under **constrained resources**.  

---  

## 🎯 **Future Work**  
✅ Enhance training with more diverse datasets.  
✅ Improve inpainting results for extreme occlusions.  
✅ Deploy a fully interactive web application.  

---  

## 📌 **Keywords**  
**GAN, Pix2Pix, cGAN, image inpainting, facial inpainting, AI restoration, deep learning, image reconstruction, AI-generated content.**  

---  
