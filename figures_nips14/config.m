MATLAB.Color.yellow = [1 1 0];
MATLAB.Color.magenta = [1 0 1];
MATLAB.Color.orange = [0 1 1];
MATLAB.Color.cyan = [0 1 1]; % cyan
MATLAB.Color.cyanMed = [0 0.6 0.6]; % cyanMed
MATLAB.Color.cyanDark = [0 0.3 0.3]; % cyanDark
MATLAB.Color.red = [1 0 0];
MATLAB.Color.redMed = [0.6 0 0];
MATLAB.Color.redDark = [0.3 0 0];
MATLAB.Color.green = [0 1 0];
MATLAB.Color.blue = [0 0 1];
MATLAB.Color.white = [1 1 1];
MATLAB.Color.black = [0 0 0];
MATLAB.Color.orange = [255 150 0]./255;
MATLAB.Color.orangeLight = [255 170 0]./255;
MATLAB.Color.orangeMed = [255 140 0]./255;
MATLAB.Color.orangeDark = [255 110 0]./255;
MATLAB.Color.greenMed = [45 125 45]./255;
MATLAB.Color.greenDark = [22 62 22]./255; % green medium
MATLAB.Color.greyDark = [90 90 90]./255;
MATLAB.Color.greyMed = [160 160 160]./255;
MATLAB.Color.greyLight = [230 230 230]./255;
MATLAB.Color.orange2 = [225 122 0]./255; % orange
MATLAB.Color.brown = [128 64 0]./255; % brown
MATLAB.Color.brownLight = [255 128 0]./255; % brown light
MATLAB.Color.brownDark = [64 32 0]./255; % brown dark

% size and position of the figures
conf.figure_width = 900;
conf.figure_height = 600;
conf.figure_position = [1 1 conf.figure_width conf.figure_height];

% line width, marker size, font size
conf.lw = 3;
conf.ms = 12;
conf.fs = 18;

% Selective Search
SS.color = MATLAB.Color.greyMed;
SS.legend = 'Selective Search (fast mode) [??]';

% BING
BING.color = MATLAB.Color.brownDark;
BING.legend = 'BING (MAXBGR) [??]';

% Obfuscation Search (bboxes, TopC=5)
OBFStopC.color = MATLAB.Color.red;
OBFStopC.legend = 'Obfuscation Search bboxes, TopC=5 (our method)';

% Obfuscation Search (bboxes, GT)
OBFSgt.color = MATLAB.Color.redMed;
OBFSgt.legend = 'Obfuscation Search bboxes, GT (our method)';

% SlidingWindow heatmap
SWheat.color = MATLAB.Color.greyMed;
SWheat.legend = 'Sliding Window heatmap';

% SlidingWindow
SW.color = MATLAB.Color.orangeLight;
SW.legend = 'Sliding Window';

% GT detection
GTdet.color = MATLAB.Color.green;
GTdet.legend = 'Ground truth';

% Info 200-classes detection
classs_list_200 = {...
    'n01930112';'n03461385';'n01688243';'n02120505';'n04067472';'n02119022';'n03673027';'n03126707';...
    'n03494278';'n07749582';'n01641577';'n07747607';'n02802426';'n03930630';'n02107142';'n03724870';...
    'n01692333';'n02115641';'n04562935';'n02111500';'n02672831';'n02110627';'n02113023';'n02256656';...
    'n04579145';'n03710193';'n02484975';'n02087394';'n04409515';'n02093859';'n02111129';'n04141975';...
    'n03372029';'n03133878';'n03733805';'n01798484';'n04560804';'n02950826';'n03935335';'n04141076';...
    'n02483362';'n03825788';'n04501370';'n03785016';'n02906734';'n01828970';'n07720875';'n03134739';...
    'n02277742';'n01443537';'n03290653';'n01773549';'n02091032';'n03259280';'n03085013';'n01990800';...
    'n02437312';'n04355338';'n03804744';'n03874293';'n02815834';'n02108089';'n02396427';'n01616318';...
    'n02114367';'n04371430';'n02168699';'n10565667';'n04485082';'n03337140';'n04399382';'n03976657';...
    'n03792782';'n04311174';'n03787032';'n04325704';'n02177972';'n04335435';'n03832673';'n02116738';...
    'n02749479';'n02095314';'n02099712';'n03814906';'n03445777';'n06874185';'n03908714';'n03983396';...
    'n04467665';'n02128385';'n04111531';'n04254777';'n02233338';'n04209239';'n07697537';'n04311004';...
    'n02777292';'n03355925';'n02110958';'n01530575';'n02107908';'n04200800';'n04154565';'n04023962';...
    'n01514668';'n03180011';'n03131574';'n03124043';'n03902125';'n12768682';'n03775546';'n07714571';...
    'n03594734';'n02480495';'n02099267';'n03967562';'n03866082';'n03379051';'n03417042';'n02104365';...
    'n07730033';'n01729977';'n01698640';'n04252225';'n03476991';'n03796401';'n01514859';'n03729826';...
    'n03201208';'n01614925';'n07711569';'n02356798';'n07684084';'n01882714';'n04153751';'n04049303';...
    'n07718747';'n04004767';'n04591157';'n02115913';'n04447861';'n03781244';'n01693334';'n07745940';...
    'n07753592';'n01537544';'n04398044';'n04589890';'n02607072';'n04037443';'n02783161';'n02093256';...
    'n02412080';'n12267677';'n02909870';'n02165456';'n02487347';'n02108915';'n02504013';'n02106382';...
    'n03220513';'n02087046';'n03065424';'n02099601';'n02127052';'n04592741';'n03476684';'n01883070';...
    'n02102973';'n02226429';'n03347037';'n03887697';'n04428191';'n02276258';'n03733281';'n03424325';...
    'n02948072';'n02992211';'n03400231';'n04296562';'n02490219';'n03888257';'n02965783';'n03998194';...
    'n03803284';'n02206856';'n03977966';'n02086240';'n04040759';'n03670208';'n02280649';'n02441942';...
    'n03761084';'n03908618';'n02510455';'n02794156';'n02841315';'n02865351';'n02088238';'n02927161'...
};
classs_description_200 = {...
'nematode, nematode worm, roundworm';'grocery store, grocery, food market, market';...
'frilled lizard, Chlamydosaurus kingi';'grey fox, gray fox, Urocyon cinereoargenteus';...
'reel';'red fox, Vulpes vulpes';'liner, ocean liner';'crane';...
'harmonica, mouth organ, harp, mouth harp';'lemon';'bullfrog, Rana catesbeiana';...
'orange';'basketball';'pickup, pickup truck';'Doberman, Doberman pinscher';'mask';...
'Gila monster, Heloderma suspectum';'dingo, warrigal, warragal, Canis dingo';'water tower';...
'Great Pyrenees';'accordion, piano accordion, squeeze box';'affenpinscher, monkey pinscher, monkey dog';...
'Pembroke, Pembroke Welsh corgi';'cicada, cicala';'whiskey jug';'mailbox, letter box';...
'guenon, guenon monkey';'Rhodesian ridgeback';'tennis ball';'Kerry blue terrier';...
'Leonberg';'scale, weighing machine';'flute, transverse flute';'Crock Pot';'measuring cup';...
'prairie chicken, prairie grouse, prairie fowl';'water jug';'cannon';'piggy bank, penny bank';...
'sax, saxophone';'gibbon, Hylobates lar';'nipple';'turnstile';'moped';'broom';'bee eater';...
'bell pepper';'croquet ball';'ringlet, ringlet butterfly';'goldfish, Carassius auratus';...
'entertainment center';'barn spider, Araneus cavaticus';'Italian greyhound';'Dutch oven';...
'computer keyboard, keypad';'isopod';'Arabian camel, dromedary, Camelus dromedarius';...
'sundial';'nail';'paddlewheel, paddle wheel';'beaker';'boxer';'wild boar, boar, Sus scrofa';...
'vulture';'timber wolf, grey wolf, gray wolf, Canis lupus';'swimming trunks, bathing trunks';...
'long-horned beetle, longicorn, longicorn beetle';'scuba diver';'tripod';'file, file cabinet, filing cabinet';...
'teddy, teddy bear';'pole';'mountain bike, all-terrain bike, off-roader';'steel drum';...
'mortarboard';'stole';'weevil';'streetcar, tram, tramcar, trolley, trolley car';...
'notebook, notebook computer';'African hunting dog, hyena dog, Cape hunting dog, Lycaon pictus';...
'assault rifle, assault gun';'wire-haired fox terrier';'Labrador retriever';...
'necklace';'golf ball';'traffic light, traffic signal, stoplight';'pencil sharpener';...
'pop bottle, soda bottle';'trailer truck, tractor trailer, trucking rig, rig, articulated lorry, semi';...
'leopard, Panthera pardus';'rotisserie';'sock';'cockroach, roach';'shower curtain';...
'hotdog, hot dog, red hot';'steel arch bridge';'balance beam, beam';'flagpole, flagstaff';...
'pug, pug-dog';'brambling, Fringilla montifringilla';'Appenzeller';'shoe shop, shoe-shop, shoe store';...
'screwdriver';'punching bag, punch bag, punching ball, punchball';'cock';'desktop computer';...
'crib, cot';'cowboy boot';'pay-phone, pay-station';'buckeye, horse chestnut, conker';...
'mixing bowl';'head cabbage';'jean, blue jean, denim';'orangutan, orang, orangutang, Pongo pygmaeus';...
'flat-coated retriever';'plow, plough';'overskirt';'football helmet';'garbage truck, dustcart';...
'schipperke';'cardoon';'green snake, grass snake';'American alligator, Alligator mississipiensis';...
'snowplow, snowplough';'hair spray';'moving van';'hen';'matchstick';'dining table, board';...
'bald eagle, American eagle, Haliaeetus leucocephalus';'mashed potato';...
'fox squirrel, eastern fox squirrel, Sciurus niger';'French loaf';...
'koala, koala bear, kangaroo bear, native bear, Phascolarctos cinereus';'screw';...
'rain barrel';'artichoke, globe artichoke';'printer';'Windsor tie';'dhole, Cuon alpinus';...
'toilet seat';'monastery';'green lizard, Lacerta viridis';'strawberry';'banana';...
'indigo bunting, indigo finch, indigo bird, Passerina cyanea';'teapot';'window screen';...
'anemone fish';'racer, race car, racing car';'ballpoint, ballpoint pen, ballpen, Biro';...
'Staffordshire bullterrier, Staffordshire bull terrier';'ram, tup';'acorn';'bucket, pail';...
'ladybug, ladybeetle, lady beetle, ladybird, ladybird beetle';'macaque';'French bulldog';...
'Indian elephant, Elephas maximus';'Bouvier des Flandres, Bouviers des Flandres';'dome';...
'toy terrier';'coil, spiral, volute, whorl, helix';'golden retriever';'lynx, catamount';...
'wing';'hair slide';'wombat';'Irish water spaniel';'grasshopper, hopper';'fire screen, fireguard';...
'paper towel';'thresher, thrasher, threshing machine';'admiral';'maze, labyrinth';...
'gasmask, respirator, gas helmet';'candle, taper, wax light';'cello, violoncello';...
'frying pan, frypan, skillet';'stage';'marmoset';'parachute, chute';'car mirror';...
'prayer rug, prayer mat';'muzzle';'bee';'police van, police wagon, paddy wagon, patrol wagon, wagon, black Maria';...
'Shih-Tzu';'radiator';'limousine, limo';'cabbage butterfly';'weasel';'microwave, microwave oven';...
'pencil box, pencil case';'giant panda, panda, panda bear, coon bear, Ailuropoda melanoleuca';...
'barometer';'binoculars, field glasses, opera glasses';'bolo tie, bolo, bola tie, bola';...
'basset, basset hound';'butcher shop, meat market'...
};
num_classes = length(classs_list_200);