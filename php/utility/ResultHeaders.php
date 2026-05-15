<?php
declare(strict_types=1);

// FreeMusic SDK utility: result_headers

class FreeMusicResultHeaders
{
    public static function call(FreeMusicContext $ctx): ?FreeMusicResult
    {
        $response = $ctx->response;
        $result = $ctx->result;
        if ($result) {
            if ($response && is_array($response->headers)) {
                $result->headers = $response->headers;
            } else {
                $result->headers = [];
            }
        }
        return $result;
    }
}
