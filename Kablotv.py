export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const path = url.pathname.replace("/", "");
    const slug = path.split(".")[0];

    if (!slug || path === "") {
      return new Response(null, { status: 400 });
    }

    const target_api = "https://core-api.kablowebtv.com/api/channels?checkip=false";
    const headers = {
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
      "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJjZ2QiOiIwOTNkNzIwYS01MDJjLTQxZWQtYTgwZi0yYjgxNjk4NGZiOTUiLCJkaSI6IjBmYTAzNTlkLWExOWItNDFiMi05ZTczLTI5ZWNiNjk2OTY0MCIsImFwdiI6IjEuMC4wIiwiZW52IjoiTElWRSIsImFibiI6IjEwMDAiLCJzcGdkIjoiYTA5MDg3ODQtZDEyOC00NjFmLWI3NmItYTU3ZGViMWI4MGNjIiwiaWNoIjoiMCIsInNnZCI6ImViODc3NDRjLTk4NDItNDUwNy05YjBhLTQ0N2RmYjg2NjJhZCIsImlkbSI6IjAiLCJkY3QiOiIzRUY3NSIsImlhIjoiOjpmZmZmOjEwLjAuMC41IiwiY3NoIjoiVFJLU1QiLCJpcGIiOiIwIn0.bT8PK2SvGy2CdmbcCnwlr8RatdDiBe_08k7YlnuQqJE",
      "Origin": "https://kablowebtv.com",
      "Referer": "https://kablowebtv.com/"
    };

    try {
      const res = await fetch(target_api, { headers });
      const data = await res.json();
      
      const raw = data?.Data?.AllChannels?.[0]?.StreamData?.HlsStreamUrl || "";
      const match = raw.match(/wmsAuthSign=([^&]+)/);
      const sign = match ? match[1] : null;

      if (!sign) {
        return new Response(null, { status: 500 });
      }

      const redirect_url = `https://ottcdn.kablowebtv.net/live_turksat_sub3/${slug}_stream/index.m3u8?wmsAuthSign=${sign}`;

      return Response.redirect(redirect_url, 302);

    } catch (e) {
      return new Response(null, { status: 500 });
    }
  }
};
