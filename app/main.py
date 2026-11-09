from fastapi import FastAPI, File, UploadFile, HTTPException
from app.crypto import load_public_key, verify_bytes
from app.storage import save_experiments


public_key = load_public_key("keys/public_key.pem")

app = FastAPI(title="Chem Ledger")


@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/experiments")
async def upload_experiments(
    experiment: UploadFile = File(...),
    signature: UploadFile = File(...)
):
    experiment_data = await experiment.read()
    signature_data = await signature.read()

    is_valid = verify_bytes(
            experiment_data,
            signature_data,
            public_key
        )

    if not is_valid:
        raise HTTPException(
            status_code=400,
            detail="Invalid digital signature"
        )
    stored_path = save_experiments(experiment_data)

    return {
        "filename": experiment.filename,
        "file_size": len(experiment_date),
        "signature_size": len(signature_data),
        "verified": True,
        "stored": True
    }


