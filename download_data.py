import kagglehub
import os
import shutil

def main():
    # 1. Download the latest version of the dataset
    print("Downloading dataset from Kaggle...")
    path = kagglehub.dataset_download("piterfm/instagram-usage-lifestyle-2025-2026")
    
    # 2. Define your local data directory
    local_data_dir = "./data"
    if not os.path.exists(local_data_dir):
        os.makedirs(local_data_dir)
    
    # 3. Move the CSV file to your local folder
    for file in os.listdir(path):
        if file.endswith(".csv"):
            shutil.copy(os.path.join(path, file), os.path.join(local_data_dir, "instagram_usage_lifestyle.csv"))
            print(f"✅ Success! Data moved to: {local_data_dir}/instagram_usage_lifestyle.csv")

if __name__ == "__main__":
    main()
