import os
import shutil
import zipfile
from PyInstaller.__main__ import run

if __name__ == '__main__':

    #######   手工配置部分   #########################################
    # 脚本名
    script_name = 'KivviSignAppTool'
    # 图标文件，如果没有就写 None
    icon_file = 'icon.ico'

    def _clean():
        clean_dirs = ['build', 'dist']
        for dir in clean_dirs:
            shutil.rmtree(dir)

    def _copy_dir():
        dist_dirs = ['source']
        for dir in dist_dirs:
            if os.path.exists(dir):
                shutil.copytree(dir, 'dist/' +dir)

    def _get_file_name():
        file_name = 'KivviSignAppTool'
        return file_name

    def make_zip(source_dir, output_filename):
        zipf = zipfile.ZipFile(output_filename, 'w')
        pre_len = len(os.path.dirname(source_dir))
        for parent, dirnames, filenames in os.walk(source_dir):
            for filename in filenames:
                pathfile = os.path.join(parent, filename)
                arcname = pathfile[pre_len:].strip(os.path.sep)  # 相对路径
                zipf.write(pathfile, arcname)
        zipf.close()
    #################################################################

    # 想法就是如果有spec文件，就用spec, 没有再用原始脚本
    spec_file = '{}.spec'.format(script_name)
    if os.path.exists(spec_file) and os.path.isfile(spec_file):
        opts = [spec_file, '-F']
    else:
        script_file = '{}.py'.format(script_name)
        opts = ['KivviSignAppTool.py', '-F']  # 不知道为什么打包命令添加 -w 参数程序总是运行失败???
        if icon_file is not None:
            opts.append('-i')
            opts.append(icon_file)

    _copy_dir()
    run(opts)
    file_name = _get_file_name()
    make_zip('dist', file_name + '.zip')
    _clean()
