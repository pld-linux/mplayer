#
# TODO: bcond for libsmbclient and maybe libdv?
#
# Conditional build:
%bcond_with	directfb	# with DirectFB video output
%bcond_with	divx4linux	# with divx4linux a/v support (binaries, instead
				#  of included OpenDivx)

%bcond_with	dxr3		# enable use of DXR3/H+ hardware MPEG decoder
%bcond_with	ggi		# with ggi video output
%bcond_with	live		# enable use of live.com libraries
%bcond_with	nas		# with NAS audio output
%bcond_with	svga		# with svgalib video output
%bcond_with	osd		# with osd menu support
%bcond_with	theora		# with theora support

%bcond_without	altivec		# without altivec support

%bcond_without	aalib		# without aalib video output
%bcond_without	alsa		# without ALSA audio output
%bcond_without	arts		# without arts audio output
%bcond_without	dshow		# disable DirectShow support
%bcond_without	gui		# without gui gtk+ interfeace
%bcond_without	joystick	# disable joystick support
%bcond_without	lirc		# without lirc support
%bcond_without	mad		# without mad (audio MPEG) support
%bcond_without	quicktime	# without binary quicktime dll support
%bcond_without	real		# without Real* 8/9 codecs support
%bcond_without	runtime		# disable runtime cpu detection, just detect CPU
				#  in compile time (advertised by mplayer
				#  authors as working faster); in this case
				#  mplayer may not work on machine other then
				#  where it was compiled
%bcond_without	select		# disable audio select() support (for example
				# required this option ALSA or Vortex2 driver)
%bcond_without	win32		# without win32 codecs support
%bcond_without	vorbis		# without ogg-vorbis audio support

%bcond_with	gtk2		# EXPERIMENTAL support for GTK+ version 2
%bcond_with	xlibs

%ifnarch %{ix86}
%undefine	with_win32
%undefine	with_quicktime
%endif

# set it to 0, or 1
%define		snapshot	0

%define		sname		MPlayer
%define		snap		20030810
%define		ffmpeg_ver	0.4.5

%define	pre	pre3
Summary:	Yet another movie player for Linux
Summary(es):	Otro reproductor de pel�culas para Linux
Summary(ko):	�������� �̵���÷��̾�
Summary(pl):	Jeszcze jeden odtwarzacz film�w dla Linuksa
Summary(pt_BR):	Reprodutor de filmes
Name:		mplayer
Version:	1.0
Release:	0.%{pre}.7
Epoch:		1
License:	GPL
Group:		X11/Applications/Multimedia
%if %{snapshot}
#Source0:	ftp://ftp.mplayerhq.hu/%{sname}/cvs/%{sname}-%{snap}.tar.bz2
#Source0:	%{name}-%{snap}.tar.bz2
#Source1:	http://dl.sourceforge.net/ffmpeg/ffmpeg-%{ffmpeg_ver}.tar.gz
Source1:	libavcodec-%{snap}.tar.bz2
# Source1-md5:	8c32cd38df314638624bf5ef76081265
%else
Source0:	ftp://ftp3.mplayerhq.hu/%{sname}/releases/%{sname}-%{version}%{pre}.tar.bz2
# Source0-md5:	998becb79417c6a14d15c07e85188b82
%endif
Source3:	ftp://mplayerhq.hu/%{sname}/releases/fonts/font-arial-iso-8859-2.tar.bz2
# Source3-md5:	7b47904a925cf58ea546ca15f3df160c
Source4:	ftp://mplayerhq.hu/%{sname}/Skin/default-1.7.tar.bz2
# Source4-md5:	7e1d16c2f8a32469f4354cb043eecc5d
Source5:	g%{name}.desktop
Source6:	ftp://mplayerhq.hu/%{sname}/releases/fonts/font-arial-iso-8859-1.tar.bz2
# Source6-md5:	1ecd31d17b51f16332b1fcc7da36b312
Source7:	%{name}.png
Patch0:		%{name}-no_libnsl.patch
Patch1:		%{name}-cp1250-fontdesc.patch
Patch2:		%{name}-codec.patch
Patch3:		%{name}-home_etc.patch
Patch4:		%{name}-350.patch
Patch5:		%{name}-configure.patch
Patch6:		%{name}-gtk+2.patch
Patch7:		%{name}-alpha.patch
Patch8:		%{name}-altivec.patch
Patch9:		%{name}-gcc34.patch
Patch10:	%{name}-mpl2.patch
URL:		http://www.mplayerhq.hu/
%{?with_directfb:BuildRequires:	DirectFB-devel}
%{?with_divx4linux:BuildRequires:	divx4linux-devel >= 1:5.01.20020418}
%{?with_dxr3:BuildRequires:		em8300-devel}
%{?with_ggi:BuildRequires:		libggi-devel}
%{?with_live:BuildRequires:		live}
%{?with_nas:BuildRequires:		nas-devel}
%{?with_svga:BuildRequires:		svgalib-devel}
%{?with_aalib:BuildRequires:	aalib-devel}
%{?with_alsa:BuildRequires:	alsa-lib-devel}
%{?with_arts:BuildRequires:	arts-devel}
%{?with_dshow:BuildRequires:	libstdc++-devel}
%if %{with gui}
BuildRequires:		gtk+%{?with_gtk2:2}-devel
%endif
%{?with_lirc:BuildRequires:	lirc-devel}
%{?with_mad:BuildRequires:		mad-devel}
%{?with_vorbis:BuildRequires:	libvorbis-devel}
BuildRequires:	OpenGL-devel
BuildRequires:	SDL-devel >= 1.1.7
%if %{with xlibs}
BuildRequires:	libXv-devel
%else
BuildRequires:	XFree86-devel >= 4.0.2
%endif
BuildRequires:	audiofile-devel
BuildRequires:	cdparanoia-III-devel
BuildRequires:	esound-devel
#BuildRequires:	faad2-devel
BuildRequires:	freetype-devel
%ifarch ppc
%{?with_altivec:BuildRequires:	gcc >= 5:3.3.2-3}
%endif
BuildRequires:	lame-libs-devel
BuildRequires:	libdv-devel
BuildRequires:	libjpeg-devel
BuildRequires:	libmatroska-devel >= 0.6.3-2
BuildRequires:	libpng-devel
BuildRequires:	libsmbclient-devel
%{?with_theora:BuildRequires:	libtheora-devel}
BuildRequires:	libungif-devel
BuildRequires:	lzo-devel
BuildRequires:	ncurses-devel
BuildRequires:	xvid-devel >= 1:0.9.0
BuildRequires:	zlib-devel
Requires:	OpenGL
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_noautoreqdep	libGL.so.1 libGLU.so.1
%define		specflags	-fomit-frame-pointer
%define		specflags_alpha	-mmax
%if %{with altivec}
%define		specflags_ppc	-maltivec -mabi=altivec
%endif
%define		_desktopdir	%{_applnkdir}/Multimedia

%description
Movie player for Linux. Supported input formats: VCD (VideoCD),
MPEG1/2, RIFF AVI, ASF 1.0, Quicktime. Supported audio codecs: PCM
(uncompressed), MPEG layer 2/3, AC3, aLaw, MS-GSM, Win32 ACM.
Supported video codecs: MPEG 1 and MPEG 2, Win32 ICM (VfW), OpenDivX.
Supported output devices: Matrox G200/G400 hardware, Matrox G200/G400
overlay, X11 optionally with SHM extension, X11 using overlays with
the Xvideo extension, OpenGL renderer, Matrox G400 YUV support on
framebuffer Voodoo2/3 hardware, SDL v1.1.7 driver etc.

If you want to use win32 codecs install w32codec package.

%description -l es
Reproductor video para Linux. Formatos de entrada soportados: VCD
(VideoCD), MPEG1/2, RIFF AVI, ASF 1.0, Quicktime. Codecs de audio
soportados: PCM (uncompressed), MPEG layer 2/3, AC3, aLaw, MS-GSM,
Win32 ACM. Codecs de video soportados: MPEG 1 and MPEG 2, Win32 ICM
(VfW), OpenDivX. Dispositivos de salida soportados: Matrox G200/G400
hardware, Matrox G200/G400 overlay, X11 optionalmente con la extensi�n
SHM, X11 usando overlays con la extensi�n Xvideo, plasmador OpenGL,
soporte de Matrox G400 YUV en hardware de framebuffer de Voodoo2/3,
controlador SDL v1.1.7 etc.

Si quiere usar codecs Win32, instale el paquete w32codec.

%description -l ko
MPlayer�� �������� �����÷��̾��Դϴ�. ��κ��� mpeg, avi �׸��� asf
������ ����մϴ�. VCD, DVD, �� ���� DivX���� �� �� �ֽ��ϴ�.
MPlayer�� �� �ٸ� ū Ư¡�� ��� ����̹��� �پ��ϴٴ� ���Դϴ�. X11,
Xv, DGA, OpenGL, SVGAlib, fbdev�� �۵��ϸ�, SDL�̳�
(Matrox/3dfx/Sis����) Ư�� ī�忡 ���ӵ� �ο췹 �� ����̹��鵵 �����
�� �ֽ��ϴ�. ��κ��� ��� ����̹����� ����Ʈ���� Ȥ�� �ϵ��������
ũ������ (scaling)�� �����ϹǷ�, ��üȭ������ ������ ������ ��
�ֽ��ϴ�. �Ӹ��ƴ϶�, �ѱ���, ����, �밡����, ü�ھ�, ���þƾ����
�ε巯��(antialiased) �ڸ���Ʈ�� ����� �� �ֽ��ϴ�.

%description -l pl
Odtwarzacz wideo dla Linuksa. Wspierane formaty wej�ciowe: VCD
(VideoCD), MPEG1/2, RIFF AVI, ASF 1.0, Quicktime. Wspierane kodeki
audio: PCM (nieskompresowane), MPEG layer 2/3, AC3, aLaw, MS-GSM,
Win32 ACM. Wspierane kodeki wideo: MPEG 1 and MPEG 2, Win32 ICM (VfW),
OpenDivX. Wspierane urz�dzenia wyj�ciowe: Matrox G200/G400, X11
opcjonalnie z rozszerzeniem SHM, X11 z rozszerzeniem Xvideo, renderer
OpenGL, Matrox G400 u�ywaj�c framebuffera, Voodoo2/3, SDL v1.1.7 itp.

Je�li chcesz u�ywa� kodek�w win32, zainstaluj pakiet w32codec.

%description -l pt_BR
MPlayer � um reprodutor de filmes que suporta v�rios codecs de v�deo e
�udio. Diferentes mecanismos de reprodu��o podem tamb�m ser
escolhidos, incluindo SDL, SVGALib, frame buffer, aalib, X11 e outros.

%prep
%if %{snapshot}
%setup -q -n %{name}-%{snap} -a 1 -a 3 -a 6
%else
%setup -q -n %{sname}-%{version}%{pre} -a 3 -a 6
%endif

cp -f etc/codecs.conf etc/codecs.win32.conf
%patch0 -p1
%patch1 -p0
##%patch2 -p1
##%patch3 -p1	-- old home_etc behavior
%patch4 -p1
%patch5 -p1
%if %{with gtk2}
%patch6 -p1
%endif
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1

%build
CFLAGS="%{rpmcflags}"
CC="%{__cc}"
export CC CFLAGS
./configure \
			--prefix=%{_prefix} \
			--confdir=%{_sysconfdir}/mplayer \
			--with-x11incdir=/usr/X11R6/include \
			--with-extraincdir=%{_includedir}/xvid \
%ifnarch %{ix86}
			--disable-mmx \
			--disable-mmx2 \
			--disable-3dnow \
			--disable-3dnowex \
			--disable-sse \
			--disable-sse2 \
			--disable-fastmemcpy \
%endif
%ifarch ppc
%{!?with_altivec:--disable-altivec} \
%endif
%{!?with_directfb:--disable-directfb} \
%{!?with_divx4linux:--disable-divx4linux} \
%{?with_divx4linux:--with-extraincdir=/usr/include/divx} \
%{!?with_dxr3:--disable-dxr3} \
%{!?with_ggi:--disable-ggi} \
%{?with_live:--enable-live --with-livelibdir=/usr/lib/liveMedia --with-extraincdir=/usr/include/liveMedia } \
%{!?with_nas:--disable-nas} \
%{!?with_svga:--disable-svga} \
%{!?with_aalib:--disable-aa} \
%{!?with_alsa:--disable-alsa} \
%{?with_alsa:--enable-alsa --disable-select} \
%{!?with_arts:--disable-arts} \
%{!?with_dshow:--disable-dshow} \
%{?with_gui:--enable-gui} \
%{?with_joystick:--enable-joystick} \
%{!?with_lirc:--disable-lirc} \
%{!?with_mad:--disable-mad} \
%{!?with_quicktime:--disable-qtx} \
%{!?with_real:--disable-real} \
%{!?with_runtime:--disable-runtime-cpudetection} \
%{?with_runtime:--enable-runtime-cpudetection} \
%{!?with_select:--disable-select} \
%{!?with_win32:--disable-win32} \
%{!?with_vorbis:--disable-vorbis} \
%{?with_osd:--enable-menu} \
			--enable-dga \
			--enable-fbdev \
			--enable-gl \
			--enable-mga \
			--enable-mencoder \
			--enable-sdl \
			--enable-tdfxfb \
			--enable-vm \
			--enable-x11 \
			--enable-xmga \
			--enable-xv \
			--enable-xvid \
			--enable-largefiles \
			--enable-matroska \
			--language=all \
			--with-codecsdir=%{_libdir}/codecs \
			--enable-dynamic-plugins

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d \
	$RPM_BUILD_ROOT{%{_bindir},%{_pixmapsdir},%{_sysconfdir}/mplayer} \
	$RPM_BUILD_ROOT%{_mandir}/{de,es,fr,hu,pl,zh_CN,}/man1 \
	$RPM_BUILD_ROOT{%{_datadir}/mplayer/Skin,%{_libdir}/mplayer/vidix} \
	$RPM_BUILD_ROOT%{_desktopdir}

# default config files
awk '/Delete this default/{a++};{if(!a){print}}' etc/example.conf > etc/mplayer.conf
install etc/{codecs,mplayer,input}.conf $RPM_BUILD_ROOT%{_sysconfdir}/mplayer

# executables
install mplayer mencoder $RPM_BUILD_ROOT%{_bindir}
ln -sf mplayer $RPM_BUILD_ROOT%{_bindir}/gmplayer

# fonts
rm -f font-*/runme
cp -r font-* $RPM_BUILD_ROOT%{_datadir}/mplayer
ln -sf font-arial-iso-8859-2/font-arial-24-iso-8859-2 $RPM_BUILD_ROOT%{_datadir}/mplayer/font

# skin
bzip2 -dc %{SOURCE4} | tar xf - -C $RPM_BUILD_ROOT%{_datadir}/mplayer/Skin
rm -rf $RPM_BUILD_ROOT%{_datadir}/mplayer/Skin/*/CVS

# libraries
%ifarch %{ix86}
install libdha/libdha.so.0.1 $RPM_BUILD_ROOT%{_libdir}
install vidix/drivers/*.so $RPM_BUILD_ROOT%{_libdir}/mplayer/vidix
%endif

# X-files
install %{SOURCE5} $RPM_BUILD_ROOT%{_desktopdir}
install %{SOURCE7} $RPM_BUILD_ROOT%{_pixmapsdir}

# man pages
install DOCS/man/de/*.1 $RPM_BUILD_ROOT%{_mandir}/de/man1
install DOCS/man/en/*.1 $RPM_BUILD_ROOT%{_mandir}/man1
install DOCS/man/es/*.1 $RPM_BUILD_ROOT%{_mandir}/es/man1
install DOCS/man/fr/*.1 $RPM_BUILD_ROOT%{_mandir}/fr/man1
install DOCS/man/hu/*.1 $RPM_BUILD_ROOT%{_mandir}/hu/man1
install DOCS/man/pl/*.1 $RPM_BUILD_ROOT%{_mandir}/pl/man1
install DOCS/man/zh/*.1 $RPM_BUILD_ROOT%{_mandir}/zh_CN/man1
find DOCS -name CVS -print | xargs rm -rf
find DOCS -name \*1 -print | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{?with_win32: %doc etc/codecs.win32.conf}
%doc DOCS/HTML/en/*.html DOCS/tech
%lang(de) %doc DOCS/de
%lang(es) %doc DOCS/HTML/es
%lang(fr) %doc DOCS/HTML/fr
%lang(hu) %doc DOCS/hu
%lang(it) %doc DOCS/it
%lang(pl) %doc DOCS/HTML/pl
%lang(ru) %doc DOCS/HTML/ru
%lang(zh_CN) %doc DOCS/zh
%doc README AUTHORS ChangeLog
%dir %{_sysconfdir}/mplayer
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/mplayer/*.conf
%attr(755,root,root) %{_bindir}/*
%{_datadir}/mplayer
%{_mandir}/man1/*
%lang(de) %{_mandir}/de/man1/*
%lang(es) %{_mandir}/es/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(hu) %{_mandir}/hu/man1/*
%lang(pl) %{_mandir}/pl/man1/*
%lang(zh_CN) %{_mandir}/zh_CN/man1/*
%{_desktopdir}/*
%{_pixmapsdir}/*
%attr(755,root,root) %{_libdir}/*
