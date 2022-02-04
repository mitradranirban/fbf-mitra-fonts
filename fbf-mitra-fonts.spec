# SPDX-License-Identifqier: MIT

Version:   1.0.0

Release:   1

URL: https://github.com/mitradranirban/fbf-mitra-fonts

%global foundry fbf 

%global fontfamily    mitra         

%global fontlicense       GPlv3+ with exception

%global fontlicenses      LICENCE 

%global fontdocs          changelog copyright

%global fontdocsex        %{fontlicenses}

%global fontsummary       Experimental Monospace Bengali Font

%global fonts            *.ttf

%global fontconfs        68-0-%{fontpkgname}.conf

BuildRequires: fontforge 

%global fontdescription  %{expand:
This is an experimental monospace Bengali  Font with additional ISCII
 encoding for specialised applications like xterm, IE6. It can also be
used to view ISCII encoded Bangla Text without converting to Unicode. 
}

Source0:  https://raw.githubusercontent.com/mitradranirban/fbf-mitra-fonts/main/fbf-mitra-fonts-1.0.0.tar.gz

%fontpkg 

%prep

%setup -q -n %{foundry}-%{fontfamily}-fonts-%{version} 
 chmod 755 generate.pe
./generate.pe *.sfd

%build

%fontbuild

%install

%fontinstall

%check

%fontcheck

%fontfiles

%changelog

* Thu Feb 04 2022 11:36:29 +0530 Dr Anirban Mitra <mitra_anirban@yahoo.co.in> -  1.0.0-1
- Updated font to add character to be compliant with Unicode 5.0
- removed overlapping 
 
