#
# TODO
# - select which divx codec will be used (xvid, divx4linux, opnedivx)
#   (you can choose only one of it)

# Conditional build:
#
# _with_ggi		- with ggi video output
# _without_alsa		- without ALSA support
# _without_arts		- without arts support
# _without_lirc		- without lirc support
# _without_vorbis	- without ogg-vorbis support
# _without_divx4linux	- without divx4linux support (binaries, instead of included OpenDivx)
# _without_select	- disable audio select() support (for example required this option ALSA or Vortex2 driver)
# _without_win32	- disable requirement for win32 codecs
# _without_gui		- without gui gtk+ interfeace
# _without_dshow	- disable DirectShow support

# set it to 0, or 1
%define		snapshot 	0

%define		sname		MPlayer
%define		snap		20020320
%define		ffmpeg_ver	0.4.5

%ifnarch %{ix86}
%define		_without_win32	1
%endif

Summary:	Yet another movie player for Linux
Summary(pl):	Jeszcze jeden odtwarzacz film�w dla Linuksa
Name:		mplayer
Version:	0.90pre3
Release:	1
License:	GPL
Group:		X11/Applications/Multimedia
%if %{snapshot}
Source0:	ftp://ftp.mplayerhq.hu/%{sname}/cvs/%{sname}-%{snap}.tar.bz2
%else
Source0:	http://ftp2.mplayerhq.hu/%{sname}/releases/%{sname}-%{version}.tar.bz2
%endif
Source1:	http://prdownloads.sourceforge.net/ffmpeg/ffmpeg-%{ffmpeg_ver}.tar.gz
Source2:	%{name}.conf
Source3:	ftp://mplayerhq.hu/%{sname}/releases/font-arial-iso-8859-2.tar.bz2
Source4:	ftp://mplayerhq.hu/%{sname}/Skin/default.tar.bz2
Source5:	g%{name}.desktop
Patch0:		%{name}-make.patch
Patch1:		%{name}-confpath.patch
Patch2:		%{name}-configure.patch
Patch3:		%{name}-cp1250-fontdesc.patch
Patch4:		%{name}-codec.patch
Patch5:		%{name}-libpng12.patch
URL:		http://mplayer.sourceforge.net/
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.1.7
BuildRequires:	XFree86-devel >= 4.0.2
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
%{!?_without_arts:BuildRequires:	arts-devel}
%{!?_without_divx4linux:BuildRequires:	divx4linux-devel}
%{!?_without_gui:BuildRequires:		gtk+-devel}
%{?_with_ggi:BuildRequires:		libggi-devel}
%{!?_without_gui:BuildRequires:		libpng-devel}
%{!?_without_dshow:BuildRequires:	libstdc++-devel}
%{!?_without_vorbis:BuildRequires:	libvorbis-devel}
%{!?_without_lirc:BuildRequires:	lirc-devel}
BuildRequires:	audiofile-devel
BuildRequires:	esound-devel
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc

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
Odtwarzacz wideo dla Linuksa. Wspierane formaty wej�ciowe: VCD
(VideoCD), MPEG1/2, RIFF AVI, ASF 1.0. Wspierane kodeki audio: PCM
(nieskompresowane), MPEG layer 2/3, AC3, aLaw, MS-GSM, Win32 ACM.
Wspierane kodeki wideo: MPEG 1 and MPEG 2, Win32 ICM (VfW), OpenDivX.
Wspierane urz�dzenia wyj�ciowe: Matrox G200/G400, X11 opcjonalnie z
rozszerzeniem SHM, X11 z rozszerzeniem Xvideo, renderer OpenGL, Matrox
G400 u�ywaj�c framebuffera, Voodoo2/3, SDL v1.1.7 itp.

Je�li chcesz u�ywa� kodek�w win32, zainstaluj pakiet w32codec i
skopiuj codecs.win32.conf do katalogu ~/.mplayer jako codecs.conf.

%prep
%if %{snapshot}
%setup -q -n %{sname}-%{snap} -a 1 -a 3
%else
%setup -q -n %{sname}-%{version} -a 1 -a 3
%endif

%patch0 -p1
%patch1 -p1
cp -f etc/codecs.conf etc/codecs.win32.conf
%patch2 -p1
%patch3 -p0
#%patch4 -p1
%patch5 -p1

%if %{snapshot}
cp -ar ffmpeg/libavcodec/* libavcodec
%endif

%build
CFLAGS="%{rpmcflags} %{!?debug:-fomit-frame-pointer} "
if [ -f %{_pkgconfigdir}/libpng12.pc ] ; then
	CPPFLAGS="$CFLAGS `pkg-config libpng12 --cflags`"
fi
./configure \
			--prefix=%{_prefix} \
			--with-x11incdir=%{_includedir}\
			--datadir=%{_datadir}/mplayer \
			--with-win32libdir="/usr/lib/win32" \
%{!?_without_divx4linux:--with-extraincdir=/usr/include/divx} \
%{?_without_alsa:	--disable-alsa} \
%{!?_without_alsa:	--enable-alsa --disable-select} \
			--enable-dga \
			--enable-fbdev \
%{?_with_ggi:		--enable-ggi} \
%{!?_with_ggi:		--disable-ggi} \
			--enable-gl \
%{!?_without_gui:	--enable-gui} \
%{!?_without_lirc:	--enable-lirc} \
%{?_without_lirc:	--disable-lirc} \
			--enable-mga \
			--enable-sdl \
			--enable-runtime-cpudetection \
			--enable-tdfxfb \
			--enable-vm \
%{!?_without_vorbis:	--enable-vorbis} \
%{?_without_vorbis:	--disable-vorbis} \
			--enable-xv \
			--enable-xvid \
			--enable-x11 \
			--enable-xmga \
%{?_without_divx4linux: --disable-divx4linux} \
%{?_without_select:	--disable-select} \
%{?_without_win32:	--disable-win32} \
%{?_without_dshow:	--disable-dshow} 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sysconfdir}/mplayer,%{_bindir},%{_libdir}/mplayer/vidix,%{_mandir}/{,hu/}man1} \
	$RPM_BUILD_ROOT{%{_applnkdir}/Multimedia,%{_datadir}/mplayer/{arial-{14,18,24,28},Skin}}

perl -p -i -e 'exit if /this default/' etc/example.conf
install %{SOURCE2} $RPM_BUILD_ROOT%{_sysconfdir}/mplayer/mplayer.conf
install etc/codecs.conf	$RPM_BUILD_ROOT%{_sysconfdir}/mplayer/codecs.conf
install mplayer $RPM_BUILD_ROOT%{_bindir}
install mencoder $RPM_BUILD_ROOT%{_bindir}
install libdha/libdha-0.1.so $RPM_BUILD_ROOT/%{_libdir}
ln -sf libdha-0.1.so $RPM_BUILD_ROOT/%{_libdir}/libdha.so
install vidix/drivers/*.so $RPM_BUILD_ROOT/%{_libdir}/mplayer/vidix
ln -sf mplayer $RPM_BUILD_ROOT%{_bindir}/gmplayer
install font-arial-14-iso-8859-2/*.{desc,raw} $RPM_BUILD_ROOT%{_datadir}/mplayer/arial-14
install font-arial-18-iso-8859-2/*.{desc,raw} $RPM_BUILD_ROOT%{_datadir}/mplayer/arial-18
install font-arial-24-iso-8859-2/*.{desc,raw} $RPM_BUILD_ROOT%{_datadir}/mplayer/arial-24
install font-arial-28-iso-8859-2/*.{desc,raw} $RPM_BUILD_ROOT%{_datadir}/mplayer/arial-28
ln -sf arial-24 $RPM_BUILD_ROOT%{_datadir}/mplayer/font
bzip2 -dc %{SOURCE4} | tar xf - -C $RPM_BUILD_ROOT%{_datadir}/mplayer/Skin
install DOCS/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install DOCS/Hungarian/*.1 $RPM_BUILD_ROOT%{_mandir}/hu/man1
install %{SOURCE5} $RPM_BUILD_ROOT%{_applnkdir}/Multimedia

gzip -9nf DOCS/{DVB,DXR3,Polish/DVB,French/exemple.conf}
gzip -9nf etc/{example,codecs.win32}.conf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DOCS/*.gz DOCS/*.html
%doc etc/example.conf.gz
%{?!_without_win32: %doc etc/codecs.win32.conf.gz}
%lang(de) %doc DOCS/German
%lang(hu) %doc DOCS/Hungarian
%lang(pl) %doc DOCS/Polish
%lang(fr) %doc DOCS/French
%dir %{_sysconfdir}/mplayer
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/mplayer/*.conf
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mplayer
%{_mandir}/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%{_applnkdir}/*/*
%{_libdir}
