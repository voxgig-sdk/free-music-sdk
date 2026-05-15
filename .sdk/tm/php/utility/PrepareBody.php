<?php
declare(strict_types=1);

// FreeMusic SDK utility: prepare_body

class FreeMusicPrepareBody
{
    public static function call(FreeMusicContext $ctx): mixed
    {
        if ($ctx->op->input === 'data') {
            return ($ctx->utility->transform_request)($ctx);
        }
        return null;
    }
}
