#
# Conditional build:
# _with_3dnow		- with 3Dnow! support
# _with_3dnowex		- with 3Dnow-dsp! support (K7)
# _with_sse		- with SSE support
# _with_mmx		- with MMX support
# _with_mmx2		- with MMX2 support
# _without_alsa - without ALSA support
# _without_select	- disable audio select() support ( for example required this option ALSA or Vortex2 driver )
#

%define sname MPlayer

Summary:	Yet another movie player for linux
Summary(pl):	Jeszcze jeden odtwarzacz filmów dla Linuksa
Name:		mplayer
Version:	0.18
Release:	2.pre5
License:	GPL
Group:		X11/Applications/Multimedia
Group(de):	X11/Applikationen/Multimedia
Group(pl):	X11/Aplikacje/Multimedia
Source0:	http://mplayerhq.banki.hu/MPlayer/releases/%{sname}-%{version}pre5.tgz
Source1:	%{name}.conf
Patch0:		%{name}-make.patch
Patch1:		%{name}-confpath.patch
URL:		http://mplayer.sourceforge.net/
Requires:	avi-codecs
Requires:	OpenGL
BuildRequires:	SDL-devel >= 1.1.7
BuildRequires:	XFree86-devel >= 4.0.2
BuildRequires:	OpenGL-devel
BuildRequires:	ncurses-devel
%{!?_without_alsa:BuildRequires:	alsa-lib-devel}
BuildRequires:	arts-devel
BuildRequires:	esound-devel
BuildRequires:	audiofile-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
ExclusiveArch:	%{ix86}

%define 	_noautoreqdep	libGL.so.1 libGLU.so.1
%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man
%define		_sysconfdir	/etc

%description
Movie player for linux. Supported input formats: VCD (VideoCD),
MPEG1/2, RIFF AVI, ASF 1.0. Supported audio codecs: PCM
(uncompressed), MPEG layer 2/3, AC3, aLaw, MS-GSM, Win32 ACM.
Supported video codecs: MPEG 1 and MPEG 2, Win32 ICM (VfW), OpenDivX.
Supported output devices: Matrox G200/G400 hardware, Matrox G200/G400
overlay, X11 optionally with SHM extension, X11 using overlays with
the Xvideo extension, OpenGL renderer, Matrox G400 YUV support on
framebuffer Voodoo2/3 hardware, SDL v1.1.7 driver etc.

%description -l pl
Odtwarzacz wideo dla Linuksa. Wspierane formaty wej¶ciowe: VCD
(VideoCD), MPEG1/2, RIFF AVI, ASF 1.0. Wspierane kodeki audio: PCM
(nieskompresowane), MPEG layer 2/3, AC3, aLaw, MS-GSM, Win32 ACM.
Wspierane kodeki wideo: MPEG 1 and MPEG 2, Win32 ICM (VfW), OpenDivX.
Wspierane urz±dzenia wyj¶ciowe: Matrox G200/G400, X11 opcjonalnie z
rozszerzeniem SHM, X11 z rozszerzeniem Xvideo, renderer OpenGL, Matrox
G400 u¿ywaj±c framebuffera, Voodoo2/3, SDL v1.1.7 itp.

%prep
%setup  -q -n %{sname}-%{version}pre5
%patch0 -p1
%patch1 -p1

%build
%configure \
	--with-win32libdir="/usr/lib/win32" \
%ifarch i586 i686
%{?_with_mmx:	--enable-mmx} \
%{?_with_3dnow:	--enable-3dnow} \
%{?_with_3dnowex:	--enable-3dnowex} \
%{?_with_sse:	--enable-sse} \
%{?_with_mmx2:	--enable-mmx2} \
%endif
	%{!?_without_alsa:--enable-alsa} \
	--enable-gl \
	--enable-dga \
	--enable-xv \
	--enable-vm \
	--enable-x11 \
	--enable-mga \
	--enable-xmga \
	--enable-sdl \
	--enable-fbdev \
	--enable-termcap \
%{?_without_select:	--disable-select} 

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man1,%{_sysconfdir}/mplayer}

install mplayer		$RPM_BUILD_ROOT%{_bindir}
install DOCS/*.1	$RPM_BUILD_ROOT%{_mandir}/man1
install DOCS/example.c*	$RPM_BUILD_ROOT%{_sysconfdir}/mplayer/mplayer.conf
install DOCS/codecs.c*	$RPM_BUILD_ROOT%{_sysconfdir}/mplayer/codecs.conf

gzip -9nf DOCS/{AUTHORS,CODECS,Change*,INSTALL,LIRC,MPla*,MTRR,Open*} \
	DOCS/{README,SPEED,TODO,VIDEOCARDS,example.conf,*.txt}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc DOCS/*.gz
%dir %{_sysconfdir}/mplayer
%config(noreplace) %verify(not size mtime md5) %{_sysconfdir}/mplayer/*.conf
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
