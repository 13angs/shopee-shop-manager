from fastapi import APIRouter, Depends
from app.api.dependencies.authentication import verify_token
from app.api.dependencies.linode_object_storage import download_pdfs
from app.api.models.invoice import Invoice, InvoiceDownload
from app.api.models.response import Response

router = APIRouter()

@router.post("/api/shopee/shop/{shop_id}/invoice/download", response_model=Response)
def download_invoices(shop_id: str, invoice: Invoice, payload: dict = Depends(verify_token)):
    
    json = invoice.model_dump()
    response = InvoiceDownload(**json, shop_id=shop_id)
    url = download_pdfs(invoice.order_sn)
    response.url = url
    return Response(data=response)