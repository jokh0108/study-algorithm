function compareFunction(
  [aIndex, aPlays, _, aTotalPlays],
  [bIndex, bPlays, __, bTotalPlays]
) {
  if (aTotalPlays > bTotalPlays) {
    return -1;
  }
  if (aTotalPlays < bTotalPlays) {
    return 1;
  }
  if (aPlays > bPlays) {
    return -1;
  }
  if (aPlays < bPlays) {
    return 1;
  }
  if (aIndex < bIndex) {
    return -1;
  }
  if (aIndex > bIndex) {
    return 1;
  }
  return 0;
}

function solution(genres, plays) {
  const albumMap = genres.reduce((acc, curVal, curIndex) => {
    acc[curVal] = acc[curVal]
      ? [...acc[curVal], [curIndex, plays[curIndex], curVal]]
      : [[curIndex, plays[curIndex], curVal]];
    return acc;
  }, {});

  for (const [genre, songs] of Object.entries(albumMap)) {
    const totalPlays = songs.reduce((acc, [_, plays, __]) => {
      return acc + plays;
    }, 0);
    albumMap[genre] = albumMap[genre].map((song) => [...song, totalPlays]);
  }

  let allSongs = [];
  for (const [_, songs] of Object.entries(albumMap)) {
    allSongs = [...allSongs, ...songs.sort(compareFunction).slice(0, 2)];
  }
  const answer = allSongs.sort(compareFunction);
  return answer.map(([index, _, __, ___]) => index);
}

solution(
  ["classic", "pop", "classic", "classic", "pop"],
  [500, 600, 150, 800, 2500]
);
