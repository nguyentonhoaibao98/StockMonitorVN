# get_news

> Module nhỏ để lấy tin tài chính (tiếng Việt) cho mã cổ phiếu từ Google News.

## Cài đặt

Mở terminal trong thư mục dự án rồi chạy:

```powershell
python -m pip install -r requirements.txt
```

Nếu Python trên hệ thống của bạn là `py` (Windows), có thể dùng:

```powershell
py -3 -m pip install -r requirements.txt
```

## Sử dụng

Chạy trực tiếp file:

```powershell
python get_news\GetNews.py HPG --days 1 --max 5
```

Hoặc import hàm trong mã của bạn:

```python
from get_news import get_financial_news
news = get_financial_news('HPG', days=1, max_results=5)
```