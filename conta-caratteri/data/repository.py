# ===============================
#   Repository
# =============================== 

def get_file_content(file_path: str) -> str:
    if not file_path:
        raise ValueError("Il file path non può essere vuoto!")

    try:
        with open(file_path, "r") as f:
            return f.read()

    except FileNotFoundError:
        raise FileNotFoundError("Il file non esiste")
