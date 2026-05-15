<?php
declare(strict_types=1);

// FreeMusic SDK utility: feature_add

class FreeMusicFeatureAdd
{
    public static function call(FreeMusicContext $ctx, mixed $f): void
    {
        $ctx->client->features[] = $f;
    }
}
