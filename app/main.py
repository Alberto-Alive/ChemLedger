from fastapi import FastAPI, File, UploadFile

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

    return {
        "filename": experiment.filename,
        "file_size": len(experiment_date),
        "signature_size": len(signature_data)
    }