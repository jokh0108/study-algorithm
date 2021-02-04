
SELECT `user`.id, CONCAT(IFNULL(`character`.title, ''), `character`.job, ' ', `user`.name) FROM `character`
JOIN `user`
ON `character`.user_id = `user`.id
ORDER BY `user`.id DESC