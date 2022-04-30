
AV.init({
  appId: "pPObpvTV7pQB9poQHO1NJoMP-MdYXbMMI",
  appKey: "pShwYQQ4JVfSStc56MvkHNrr",
});

var currentProduct=null;

const E = window.wangEditor;
const editor = new E('#editor');
editor.config.lang = 'en';
// 引入 i18next 插件


editor.i18next = window.i18next;


editor.config.customUploadImg = function (resultFiles, insertImgFn) {
    // resultFiles 是 input 中选中的文件列表
    // insertImgFn 是获取图片 url 后，插入到编辑器的方法
    const file = new AV.File(resultFiles[0].name, resultFiles[0]);
    file.save().then((file) => {
        insertImgFn(file.get("url"))
    }, (error) => {
        // 保存失败，可能是文件无法被读取，或者上传过程中出现问题
    });
    };

editor.config.customUploadVideo = function (resultFiles, insertVideoFn) {
    // resultFiles 是 input 中选中的文件列表
    // insertVideoFn 是获取视频 url 后，插入到编辑器的方法

    // 上传视频，返回结果，将视频地址插入到编辑器中
        const file = new AV.File(resultFiles[0].name, resultFiles[0]);
    file.save().then((file) => {
        insertImgFn(file.get("url"))
    }, (error) => {
        // 保存失败，可能是文件无法被读取，或者上传过程中出现问题
    });
}

editor.create();

function loadProduct(product){
    document.getElementById('title').value=product.get('title').get('english')
    document.getElementById('description').value=product.get('description').get('english')
    document.getElementById('cover').src=product.get('cover').url()
    editor.txt.html(product.get('detail').get('englishHTML'))
    currentProduct=product
    getCategoryByProduct(product.id,function (maps) {
        console.log(maps)
        maps.forEach(function (scm, i, a) {
            const id = scm.get('category').id;
            document.getElementById(id).classList.add('choose')
        });
    })
}

async function submit() {
    //2022年3月24号14:20金深远开始玩原神
    if (currentProduct) {
        updateEnglishProduct(currentProduct, $('#title').val(), $('#description').val(), editor.txt.html());
        const buttons = $('.cLabel.choose');
        // console.log($('.cLabel.choose').size())
        // for(i in buttons){
        //     console.log(i)
        // }
        // console.log(buttons)
        const l = [];
        buttons.each(function (a, b) {
            // console.log(b)
            l.push(b.id);

        });
        setProductCategory(currentProduct.id, l);
        if (document.getElementById('fileField').files.length !== 0) {
            setProductCover(currentProduct.id, document.getElementById('fileField').files)
        }
        alert('Successfully submit the change!');
    } else {
        currentProduct=await createProduct( editor.txt.html(),$('#title').val(),$('#description').val(),0)
        console.log(currentProduct)

        if (currentProduct) {
        updateEnglishProduct(currentProduct, $('#title').val(), $('#description').val(), editor.txt.html());
        const buttons = $('.cLabel.choose');
        // console.log($('.cLabel.choose').size())
        // for(i in buttons){
        //     console.log(i)
        // }
        // console.log(buttons)
        const l = [];
        buttons.each(function (a, b) {
            // console.log(b)
            l.push(b.id);

        });
        setProductCategory(currentProduct.id, l);
        if (document.getElementById('fileField').files.length !== 0) {
            setProductCover(currentProduct.id, document.getElementById('fileField').files)
        }
        alert('Successfully submit the change!');
    }
    }
}