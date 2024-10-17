-- Listing all the bands with Glam rock like their style,
-- rankeing by their longevity
-- Columns names must be: band_name & lifespan

SELECT band_name, (IFNULL(split, '2020') - formed) AS lifespan
FROM metal_bands
WHERE FIND_IN_SET('Glam rock', IFNULL(style, "")) > 0
ORDER BY lifespan DESC;
