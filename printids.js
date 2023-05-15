// Was hard to make, but I figured it out, (kinda) lol I just looked for some help on YouTube.
const postIDs = Array.from(document.querySelectorAll('[class*="postid-"]'))
  .map(element => element.className.match(/postid-(\d{4})/))
  .filter(match => match !== null)
  .map(match => match[1]);

postIDs.forEach(postID => console.log('Found your post ID:', postID));
