# FreeMusic SDK utility: feature_add
module FreeMusicUtilities
  FeatureAdd = ->(ctx, f) {
    ctx.client.features << f
  }
end
