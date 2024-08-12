requirejs.config({
  'baseUrl': 'src',

});

let viewer;
let pv;
require(['pv'], function (PV) {

  pv = PV;
  color = pv.color;
  viewer = pv.Viewer(document.getElementById('viewer'), {
    color: color.ssSuccession(),
    width: 'auto', height: 'auto', antialias: true,
    outline: true, quality: 'medium', style: 'hemilight',
    selectionColor: 'red', background: "",
    animateTime: 500, doubleClick: null
  });

  // viewer.options('selectionColor', '#f00');
  // viewer.setOpacity(0.5);
  pv.io.fetchPdb('1ake.pdb', function (s) {
    viewer.on('viewerReady', function () {
      viewer.cartoon('crambin', s, { color: pv.color.ssSuccession(), showRelated: '1' });
      // viewer.ballsAndSticks('crambin', s, { showRelated: '1', 'scale': '0.1' });
      // viewer.setZoom(1000.0, 1.0)
      viewer.spin(Math.PI / 8, [0, 1, 0]);
      viewer.autoZoom(1);
      viewer.fitParent()
      // viewer.setBackgroundColor('red');
      // viewer.backgroundOpacity(0.5);
      viewer.rockAndRoll(true);
    });
  });



});
