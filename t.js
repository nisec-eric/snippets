function t2d(ms) {
    return new Date(parseInt(ms)*1000).toISOString().slice(11, 11+8);
}

function d2t(data){
  var hh = data.split(":");
  return parseInt(hh[0])*3600+parseInt(hh[1])*60+parseInt(hh[2]) ;
}
