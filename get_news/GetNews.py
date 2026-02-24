from GoogleNews import GoogleNews
from newspaper import Article
from typing import List, Dict
import argparse
import json


def get_financial_news(symbol: str, days: int = 1, max_results: int = 5) -> List[Dict]:
    """
    Tìm kiếm tin tức về mã cổ phiếu trên Google News (tiếng Việt).

    Args:
        symbol: Mã cổ phiếu (ví dụ: "HPG").
        days: Số ngày gần đây để tìm (mặc định 1).
        max_results: Số bài tối đa trả về (mặc định 5).

    Returns:
        Danh sách dict chứa `title`, `source`, `published_date`, `content`, `link`.
    """
    googlenews = GoogleNews(lang='vi', region='VN', period=f'{days}d')

    search_term = f"Cổ phiếu {symbol}"
    googlenews.search(search_term)

    results = googlenews.result()
    news_data: List[Dict] = []

    print(f"Tìm thấy {len(results)} bài viết cho {symbol}...")

    for item in results[:max_results]:
        url = item.get('link')
        try:
            if not url:
                continue
            article = Article(url)
            article.download()
            article.parse()

            news_data.append({
                "title": item.get('title'),
                "source": item.get('media'),
                "published_date": item.get('date'),
                "content": (article.text[:1000] + "...") if article.text else "",
                "link": url,
            })
        except Exception as e:
            print(f"Lỗi khi đọc bài từ {url}: {e}")
            continue

    return news_data


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Lấy tin tài chính từ Google News (tiếng Việt)')
    parser.add_argument('symbol', help='Mã cổ phiếu, ví dụ: HPG')
    parser.add_argument('--days', type=int, default=1, help='Số ngày để tìm (mặc định 1)')
    parser.add_argument('--max', type=int, default=5, help='Số bài tối đa (mặc định 5)')

    args = parser.parse_args()
    news = get_financial_news(args.symbol, days=args.days, max_results=args.max)
    print(json.dumps(news, ensure_ascii=False, indent=2))
