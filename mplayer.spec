#
# TODO
# - select which divx codec will be used (xvid, divx4linux, opnedivx)
#   (you can choose only one of it)

# Conditional build:
#
# _without_lirc		- without lirc support
# _without_gui		- without gui gtk+ interfeace
# _without_win32	- disable requirement for win32 codecs
# _without_dshow	- disable DirectShow support
# _without_divx4linux	- without divx4linux support (binaries, instead of included OpenDivx)
# _without_vorbis	- without ogg-vorbis support
# _with_ggi		- with ggi video output
# _without_arts		- without arts support
# _without_alsa		- without ALSA support
# _without_select	- disable audio select() support (for example required this option
#                         ALSA or Vortex2 driver)
# _without_runtime	- disable runtime cpu detection, just detect CPU in
#			  compiletime (advertised by mplayer authors as
#			  working faster); in this case mplayer may not
#			  work on machine other then where it was compiled
# _without_dxr3		- disable use of DXR3/H+ hardware MPEG decoder

# set it to 0, or 1
%define		snapshot	0

%define		sname		MPlayer
%define		snap		20020602
%define		ffmpeg_ver	0.4.5

%ifnarch %{ix86}
%define		_without_win32	1
%define		_without_divx4linux 1
%endif

Summary:	Yet another movie player for Linux
Summary(pl):	Jeszcze jeden odtwarzacz filmów dla Linuksa
Summary(pt_BR):	Reprodutor de filmes
Name:		mplayer
Version:	0.90pre6
Release:	3
License:	GPL
Group:		X11/Applications/Multimedia
%if %{snapshot}
Source0:	ftp://ftp.mplayerhq.hu/%{sname}/cvs/%{sname}-%{snap}.tar.bz2
%else
Source0:	http://ftp2.mplayerhq.hu/%{sname}/releases/%{sname}-%{version}.tar.bz2
%endif
Source1:	http://belnet.dl.sourceforge.net/sourceforge/ffmpeg/ffmpeg-%{ffmpeg_ver}.tar.gz
Source2:	%{name}.conf
Source3:	ftp://mplayerhq.hu/%{sname}/releases/font-arial-iso-8859-2.tar.bz2
Source4:	ftp://mplayerhq.hu/%{sname}/Skin/default.tar.bz2
Source5:	g%{name}.desktop
Source6:	ftp://mplayerhq.hu/%{sname}/releases/font-arial-iso-8859-1.tar.bz2
Patch0:		%{name}-make.patch
Patch2:		%{name}-no_libnsl.patch
Patch3:		%{name}-cp1250-fontdesc.patch
Patch4:		%{name}-codec.patch
Patch5:		%{name}-libpng12.patch
Patch6:		%{name}-home_etc.patch
URL:		http://mplayer.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.1.7
BuildRequires:	XFree86-devel >= 4.0.2
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
%{!?_without_arts:BuildRequires:	arts-devel}
BuildRequires:	audiofile-devel
%{!?_without_divx4linux:BuildRequires:	divx4linux-devel}
BuildRequires:	esound-devel
%{!?_without_gui:BuildRequires:		gtk+-devel}
%{!?_without_gui:BuildRequires:		libpng-devel}
%{?_with_ggi:BuildRequires:		libggi-devel}
%{!?_without_dshow:BuildRequires:	libstdc++-devel}
%{!?_without_vorbis:BuildRequires:	libvorbis-devel}
%{!?_without_lirc:BuildRequires:	lirc-devel}
%{!?_without_dxr3:BuildRequires:	em8300-devel}
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Movie player for Linux. Supported input formats: VCD (VideoCD),
MPEG1/2, RIFF AVI, ASF 1.0. Supported audio codecs: PCM
(uncompressed), MPEG layer 2/3, AC3, aLaw, MS-GSM, Win32 ACM.
Supported video codecs: MPEG 1 and MPEG 2, Win32 ICM (VfW), OpenDivX.
Supported output devices: Matrox G200/G400 hardware, Matrox G200/G400
overlay, X11 optionally with SHM extension, X11 using overlays with
the Xvideo extension, OpenGL renderer, Matrox G400 YUV support on
framebuffer Voodoo2/3 hardware, SDL v1.1.7 driver etc.

If you want to use win32 codecs install w32codec package and copy
codecs.win32.conf to your ~/.mplayer direcory as codecs.conf.

%description -l pl
Odtwarzacz wideo dla Linuksa. Wspierane formaty wej¶ciowe: VCD
(VideoCD), MPEG1/2, RIFF AVI, ASF 1.0. Wspierane kodeki audio: PCM
(nieskompresowane), MPEG layer 2/3, AC3, aLaw, MS-GSM, Win32 ACM.
Wspierane kodeki wideo: MPEG 1 and MPEG 2, Win32 ICM (VfW), OpenDivX.
Wspierane urz±dzenia wyj¶ciowe: Matrox G200/G400, X11 opcjonalnie z
rozszerzeniem SHM, X11 z rozszerzeniem Xvideo, renderer OpenGL, Matrox
G400 u¿ywaj±c framebuffera, Voodoo2/3, SDL v1.1.7 itp.

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
%setup -q -n %{sname}-%{version} -a 1 -a 3 -a 6
%endif

%patch0 -p1
cp -f etc/codecs.conf etc/codecs.win32.conf
%patch2 -p1
%patch3 -p0
#%patch4 -p1
%patch5 -p1
%patch6 -p1

%if %{snapshot}
cp -ar ffmpeg/libavcodec/* libavcodec
%endif

%build
CFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer} "
if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
	CFLAGS="$CFLAGS `pkg-config libpng12 --cflags`"
fi
export CFLAGS
./configure \
			--prefix=%{_prefix} \
			--confdir=%{_sysconfdir}/mplayer \
			--enable-mencoder \
%{!?_without_lirc:	--enable-lirc} \
%{?_without_lirc:	--disable-lirc} \
%{!?_without_gui:	--enable-gui} \
%{?_without_win32:	--disable-win32} \
%{?_without_dshow:	--disable-dshow} \
			--enable-xvid \
%{?_without_divx4linux:	--disable-divx4linux} \
%{!?_without_vorbis:	--enable-vorbis} \
%{?_without_vorbis:	--disable-vorbis} \
%{!?_without_dxr3:	--enable-dxr3} \
%{?_without_dxr3:	--disable-dxr3} \
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
%{?_without_arts:	--disable-arts} \
%{?_without_alsa:	--disable-alsa} \
%{!?_without_alsa:	--enable-alsa --disable-select} \
%{?_without_select:	--disable-select} \
%{!?_without_win32:	--with-win32libdir=/usr/lib/win32} \
%{!?_without_divx4linux:--with-extraincdir=/usr/include/divx} \
			--disable-dvdnav

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/{,de/,hu/,pl/}man1} \
	$RPM_BUILD_ROOT{%{_sysconfdir}/mplayer,%{_datadir}/mplayer/Skin} \
	$RPM_BUILD_ROOT{%{_libdir}/mplayer/vidix,%{_applnkdir}/Multimedia}

perl -p -i -e 'exit if /this default/' etc/example.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/mplayer
install etc/codecs.conf $RPM_BUILD_ROOT%{_sysconfdir}/mplayer
install mplayer $RPM_BUILD_ROOT%{_bindir}
install mencoder $RPM_BUILD_ROOT%{_bindir}
ln -sf mplayer $RPM_BUILD_ROOT%{_bindir}/gmplayer
rm -f font-*/runme
cp -r font-* $RPM_BUILD_ROOT%{_datadir}/mplayer
ln -sf font-arial-24-iso-8859-2 $RPM_BUILD_ROOT%{_datadir}/mplayer/font
bzip2 -dc %{SOURCE4} | tar xf - -C $RPM_BUILD_ROOT%{_datadir}/mplayer/Skin
%ifarch %{ix86}
install libdha/libdha-0.1.so $RPM_BUILD_ROOT/%{_libdir}
ln -sf libdha-0.1.so $RPM_BUILD_ROOT/%{_libdir}/libdha.so
install vidix/drivers/*.so $RPM_BUILD_ROOT/%{_libdir}/mplayer/vidix
%endif
install %{SOURCE5} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia
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
%lang(fr) %doc DOCS/French
%lang(hu) %doc DOCS/Hungarian
%lang(it) %doc DOCS/Italian
%lang(pl) %doc DOCS/Polish
%dir %{_sysconfdir}/mplayer
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/mplayer/*.conf
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mplayer
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%{_applnkdir}/*/*
%attr(755,root,root) %{_libdir}/*
