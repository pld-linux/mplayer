#
# TODO
# - select which divx codec will be used (xvid, divx4linux, opnedivx)
#   (you can choose only one of it)

# Conditional build:
#
# _without_qt		- without binary qt dll support
# _without_lirc		- without lirc support
# _without_gui		- without gui gtk+ interfeace
# _without_win32	- without win32 codecs support
# _without_real		- without Real* 8/9 codecs support
# _without_dshow	- disable DirectShow support
# _with_divx4linux	- with divx4linux a/v support (binaries, instead of included OpenDivx)
# _without_mad		- without mad (audio MPEG) support
# _without_vorbis	- without ogg-vorbis audio support
# _with_directfb	- with DirectFB video output
# _with_ggi		- with ggi video output
# _with_svga		- with svgalib video output
# _without_arts		- without arts audio output
# _without_alsa		- without ALSA audio output
# _without_nas		- without NAS audio output
# _without_select	- disable audio select() support (for example required this option
#			  ALSA or Vortex2 driver)
# _without_runtime	- disable runtime cpu detection, just detect CPU in
#			  compiletime (advertised by mplayer authors as
#			  working faster); in this case mplayer may not
#			  work on machine other then where it was compiled
# _with_dxr3		- enable use of DXR3/H+ hardware MPEG decoder

# set it to 0, or 1
%define		snapshot	0

%define		sname		MPlayer
%define		snap		20021202
%define		ffmpeg_ver	0.4.5

%ifnarch %{ix86}
%define		_without_win32	1
%define		_without_qt	1
%endif

Summary:	Yet another movie player for Linux
Summary(ko):	¸®´ª½º¿ë ¹Ìµð¾îÇÃ·¹ÀÌ¾î
Summary(pl):	Jeszcze jeden odtwarzacz filmów dla Linuksa
Summary(pt_BR):	Reprodutor de filmes
Name:		mplayer
Version:	0.90rc2
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
%if %{snapshot}
Source0:	ftp://ftp.mplayerhq.hu/%{sname}/cvs/%{sname}-%{snap}.tar.bz2
#Source1:	http://belnet.dl.sourceforge.net/sourceforge/ffmpeg/ffmpeg-%{ffmpeg_ver}.tar.gz
Source1:	libavcodec-20021203.tar.bz2
%else
Source0:	ftp://ftp2.mplayerhq.hu/%{sname}/releases/%{sname}-%{version}.tar.bz2
%endif
Source2:	%{name}.conf
Source3:	ftp://mplayerhq.hu/%{sname}/releases/fonts/font-arial-iso-8859-2.tar.bz2
Source4:	ftp://mplayerhq.hu/%{sname}/Skin/default.tar.bz2
Source5:	g%{name}.desktop
Source6:	ftp://mplayerhq.hu/%{sname}/releases/fonts/font-arial-iso-8859-1.tar.bz2
Source7:	%{name}.png
Patch0:		%{name}-make.patch
Patch2:		%{name}-no_libnsl.patch
Patch3:		%{name}-cp1250-fontdesc.patch
Patch4:		%{name}-codec.patch
Patch5:		%{name}-home_etc.patch
Patch6:		%{name}-350.patch
URL:		http://mplayer.sourceforge.net/
%{?_with_directfb:BuildRequires:	DirectFB-devel}
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.1.7
BuildRequires:	XFree86-devel >= 4.0.2
BuildRequires:	aalib-devel
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
%{!?_without_arts:BuildRequires:	arts-devel}
BuildRequires:	audiofile-devel
%{?_with_divx4linux:BuildRequires:	divx4linux-devel >= 5.01.20020418}
%{?_with_dxr3:	BuildRequires:	em8300-devel}
BuildRequires:	esound-devel
%{!?_without_gui:BuildRequires:		gtk+-devel}
BuildRequires:	lame-libs-devel
%{?_with_ggi:	BuildRequires:		libggi-devel}
BuildRequires:	libjpeg-devel
BuildRequires:	libpng-devel
%{!?_without_dshow:BuildRequires:	libstdc++-devel}
BuildRequires:	libungif-devel
%{!?_without_vorbis:BuildRequires:	libvorbis-devel}
%{!?_without_lirc:BuildRequires:	lirc-devel}
BuildRequires:	lzo-devel
%{!?_without_mad:BuildRequires:	mad-devel}
%{!?_without_nas:BuildRequires:	nas-devel}
BuildRequires:	ncurses-devel
%{?_with_svga:	BuildRequires:	svgalib-devel}
BuildRequires:	xvid-devel
BuildRequires:	zlib-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Movie player for Linux. Supported input formats: VCD (VideoCD),
MPEG1/2, RIFF AVI, ASF 1.0, Quicktime. Supported audio codecs: PCM
(uncompressed), MPEG layer 2/3, AC3, aLaw, MS-GSM, Win32 ACM.
Supported video codecs: MPEG 1 and MPEG 2, Win32 ICM (VfW), OpenDivX.
Supported output devices: Matrox G200/G400 hardware, Matrox G200/G400
overlay, X11 optionally with SHM extension, X11 using overlays with
the Xvideo extension, OpenGL renderer, Matrox G400 YUV support on
framebuffer Voodoo2/3 hardware, SDL v1.1.7 driver etc.

If you want to use win32 codecs install w32codec package and copy
codecs.win32.conf to your ~/.mplayer direcory as codecs.conf.

%description -l ko
MPlayer´Â ¸®´ª½º¿ë ¹«ºñÇÃ·¹ÀÌ¾îÀÔ´Ï´Ù. ´ëºÎºÐÀÇ mpeg, avi ±×¸®°í asf
ÆÄÀÏÀ» Àç»ýÇÕ´Ï´Ù. VCD, DVD, ½É Áö¾î DivX±îÁö º¼ ¼ö ÀÖ½À´Ï´Ù.
MPlayerÀÇ ¶Ç ´Ù¸¥ Å« Æ¯Â¡Àº Ãâ·Â µå¶óÀÌ¹ö°¡ ´Ù¾çÇÏ´Ù´Â °ÍÀÔ´Ï´Ù. X11,
Xv, DGA, OpenGL, SVGAlib, fbdev¿Í ÀÛµ¿ÇÏ¸ç, SDLÀÌ³ª
(Matrox/3dfx/SisµîÀÇ) Æ¯Á¤ Ä«µå¿¡ Á¾¼ÓµÈ ·Î¿ì·¹ º§ µå¶óÀÌ¹öµéµµ »ç¿ëÇÒ
¼ö ÀÖ½À´Ï´Ù. ´ëºÎºÐÀÇ Ãâ·Â µå¶óÀÌ¹öµéÀº ¼ÒÇÁÆ®¿þ¾î È¤Àº ÇÏµå¿þ¾îÀûÀÎ
Å©±âÁ¶Àý (scaling)À» Áö¿øÇÏ¹Ç·Î, ÀüÃ¼È­¸éÀ¸·Î ¿µ»óÀ» °¨»óÇÒ ¼ö
ÀÖ½À´Ï´Ù. »Ó¸¸¾Æ´Ï¶ó, ÇÑ±¹¾î, ¿µ¾î, Çë°¡¸®¾î, Ã¼ÄÚ¾î, ·¯½Ã¾Æ¾îµîÀÇ
ºÎµå·¯¿î(antialiased) ÀÚ¸·ÆùÆ®µµ »ç¿ëÇÒ ¼ö ÀÖ½À´Ï´Ù.


%description -l pl
Odtwarzacz wideo dla Linuksa. Wspierane formaty wej¶ciowe: VCD
(VideoCD), MPEG1/2, RIFF AVI, ASF 1.0, Quicktime. Wspierane kodeki
audio: PCM (nieskompresowane), MPEG layer 2/3, AC3, aLaw, MS-GSM,
Win32 ACM. Wspierane kodeki wideo: MPEG 1 and MPEG 2, Win32 ICM (VfW),
OpenDivX. Wspierane urz±dzenia wyj¶ciowe: Matrox G200/G400, X11
opcjonalnie z rozszerzeniem SHM, X11 z rozszerzeniem Xvideo, renderer
OpenGL, Matrox G400 u¿ywaj±c framebuffera, Voodoo2/3, SDL v1.1.7 itp.

Je¶li chcesz u¿ywaæ kodeków win32, zainstaluj pakiet w32codec i
skopiuj codecs.win32.conf do katalogu ~/.mplayer jako codecs.conf.

%description -l pt_BR
MPlayer é um reprodutor de filmes que suporta vários codecs de vídeo e
áudio. Diferentes mecanismos de reprodução podem também ser
escolhidos, incluindo SDL, SVGALib, frame buffer, aalib, X11 e outros.

%prep
%if %{snapshot}
%setup -q -n %{sname}-%{snap} -a 1 -a 3 -a 6
%else
%setup -q -n %{sname}-%{version} -a 3 -a 6
%endif

%patch0 -p1
cp -f etc/codecs.conf etc/codecs.win32.conf
%patch2 -p1
%patch3 -p0
#%patch4 -p1
%patch5 -p1
%patch6 -p1

%build
CFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer}"
CC="%{__cc}"
export CC CFLAGS
./configure \
			--prefix=%{_prefix} \
			--confdir=%{_sysconfdir}/mplayer \
			--with-x11incdir=/usr/X11R6/include \
			--enable-mencoder \
%{!?_without_lirc:	--enable-lirc} \
%{?_without_lirc:	--disable-lirc} \
%{!?_without_gui:	--enable-gui} \
%{?_without_win32:	--disable-win32} \
%{?_without_dshow:	--disable-dshow} \
			--with-extraincdir=/usr/include/xvid \
			--enable-xvid \
%{!?_with_divx4linux:	--disable-divx4linux} \
%{!?_without_vorbis:	--enable-vorbis} \
%{?_without_vorbis:	--disable-vorbis} \
%{?_without_mad:	--disable-mad} \
%{?_with_dxr3:		--enable-dxr3} \
%{!?_with_dxr3:		--disable-dxr3} \
%ifnarch %{ix86}
			--disable-mmx \
			--disable-mmx2 \
			--disable-3dnow \
			--disable-3dnowex \
			--disable-sse \
			--disable-sse2 \
			--disable-fastmemcpy \
%endif
%{?_without_runtime:	--disable-runtime-cpudetection} \
%{!?_without_runtime:	--enable-runtime-cpudetection} \
			--enable-gl \
			--enable-dga \
			--enable-sdl \
%{?_with_ggi:		--enable-ggi} \
%{!?_with_ggi:		--disable-ggi} \
			--enable-mga \
			--enable-xmga \
			--enable-xv \
			--enable-vm \
			--enable-x11 \
			--enable-fbdev \
			--enable-tdfxfb \
%{!?_with_directfb:	--disable-directfb} \
%{!?_with_svga:		--disable-svga} \
%{?_without_nas:	--disable-nas} \
%{?_without_arts:	--disable-arts} \
%{?_without_alsa:	--disable-alsa} \
%{!?_without_alsa:	--enable-alsa --disable-select} \
%{?_without_select:	--disable-select} \
%{!?_without_win32:	--with-win32libdir=/usr/lib/win32} \
%{!?_without_real:	--with-reallibdir=/usr/lib/win32} \
%{!?_without_real:	--enable-real} \
%{?_with_divx4linux:	--with-extraincdir=/usr/include/divx} \
%{!?_without_qt:	--enable-qtx-codecs} \
			--disable-dvdnav

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{,de/,hu/,pl/}man1} \
	$RPM_BUILD_ROOT{%{_sysconfdir}/mplayer,%{_datadir}/mplayer/Skin} \
	$RPM_BUILD_ROOT{%{_libdir}/mplayer/vidix,%{_applnkdir}/Multimedia} \
	$RPM_BUILD_ROOT%{_pixmapsdir}

perl -p -i -e 'exit if /this default/' etc/example.conf
install %{SOURCE2} etc/codecs.conf $RPM_BUILD_ROOT%{_sysconfdir}/mplayer
install mplayer mencoder $RPM_BUILD_ROOT%{_bindir}
ln -sf mplayer $RPM_BUILD_ROOT%{_bindir}/gmplayer
rm -f font-*/runme
cp -r font-* $RPM_BUILD_ROOT%{_datadir}/mplayer
ln -sf font-arial-24-iso-8859-2 $RPM_BUILD_ROOT%{_datadir}/mplayer/font
bzip2 -dc %{SOURCE4} | tar xf - -C $RPM_BUILD_ROOT%{_datadir}/mplayer/Skin
rm -rf $RPM_BUILD_ROOT%{_datadir}/mplayer/Skin/*/CVS
%ifarch %{ix86}
install libdha/libdha.so* $RPM_BUILD_ROOT/%{_libdir}
install vidix/drivers/*.so $RPM_BUILD_ROOT/%{_libdir}/mplayer/vidix
%endif
install %{SOURCE5} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia
install %{SOURCE7} $RPM_BUILD_ROOT%{_pixmapsdir}
install DOCS/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
mv DOCS/German/*.1 $RPM_BUILD_ROOT%{_mandir}/de/man1
mv DOCS/Hungarian/*.1 $RPM_BUILD_ROOT%{_mandir}/hu/man1
mv DOCS/Polish/*.1 $RPM_BUILD_ROOT%{_mandir}/pl/man1

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DOCS/*.html
%doc etc/example.conf
%{?!_without_win32: %doc etc/codecs.win32.conf}
%lang(de) %doc DOCS/German
#%lang(fr) %doc DOCS/French
%lang(hu) %doc DOCS/Hungarian
%lang(it) %doc DOCS/Italian
%lang(pl) %doc DOCS/Polish
%doc AUTHORS ChangeLog
%dir %{_sysconfdir}/mplayer
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/mplayer/*.conf
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mplayer
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_applnkdir}/*/*
%{_pixmapsdir}/*
%attr(755,root,root) %{_libdir}/*
