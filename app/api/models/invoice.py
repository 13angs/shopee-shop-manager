from typing import Optional
from pydantic import BaseModel

class Invoice(BaseModel):
    type: str = None
    order_sn: Optional[list] = []

class InvoiceDownload(Invoice): 
    url: Optional[str] = None
    shop_id: Optional[str] = None