<?php
declare(strict_types=1);

// FreeMusic SDK utility: result_body

class FreeMusicResultBody
{
    public static function call(FreeMusicContext $ctx): ?FreeMusicResult
    {
        $response = $ctx->response;
        $result = $ctx->result;
        if ($result && $response && $response->json_func && $response->body) {
            $result->body = ($response->json_func)();
        }
        return $result;
    }
}
