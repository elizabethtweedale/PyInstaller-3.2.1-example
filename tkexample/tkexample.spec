# -*- mode: python -*-

block_cipher = None


a = Analysis(['../tkexample.py'],
             pathex=['/Users/elizabethtweedale/Python/PyInstaller-3.2.1/tkexample'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='tkexample',
          debug=False,
          strip=False,
          upx=True,
          console=False )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='tkexample')
app = BUNDLE(coll,
             name='tkexample.app',
             icon=None,
             bundle_identifier=None)
