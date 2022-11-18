import fire

def process_pictures(picture_folder_path, days_back=10, process_faces=False):
    print("Doing work...This is a log")
    print(f"{picture_folder_path=}, {days_back=}, {process_faces=}")

    for i in range(0, 10):
        print(f"Doing work...This is a log {i}")
        
    return True

if __name__ == "__main__":
    fire.Fire(process_pictures)