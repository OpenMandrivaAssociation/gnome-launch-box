%define	name	gnome-launch-box
%define version	0.2
%define	release	%mkrel 1

Name:		%name
Version:	%version
Release:	%release
Summary:	GNOME Launch Box
License:	GPL
Group:		Graphical desktop/GNOME
URL:		http://developer.imendio.com/projects/gnome-launch-box
Source:		%{name}-%{version}.tar.bz2
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	gtk2-devel >= 2.6.0
BuildRequires:	libgnomeui2-devel >= 2.10.0
BuildRequires:	libglade2.0-devel >= 2.5.0
BuildRequires:	libwnck-devel >= 2.10.0
BuildRequires:	autoconf2.5
BuildRequires:	perl(XML::Parser)
BuildRequires:	gnome-doc-utils >= 0.3.2
BuildRequires:  gnome-menus-devel
BuildRequires:  evolution-data-server-devel
BuildRequires:  gnome-desktop-devel
Requires:	gnome-mime-data
Requires:	gnome-icon-theme
Requires(pre):	GConf2
Requires(post):	GConf2
Requires(post): scrollkeeper
Requires(preun):  GConf2
Requires(postun): scrollkeeper

%description
Launch Box is generally an application launcher. It's very influenced 
by Quicksilver for Mac OSX. Remember that this is only a first release 
so don't get your hopes up too much.

%prep
%setup -q

%build
%configure2_5x

%make

%install
rm -rf $RPM_BUILD_ROOT
export GCONF_DISABLE_MAKEFILE_SCHEMA_INSTALL=1
%makeinstall_std

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%define schemas %name

%post
%post_install_gconf_schemas %{schemas}

%preun
%preun_uninstall_gconf_schemas %{schemas}

%files -f %{name}.lang
%defattr(-,root,root)
%doc AUTHORS ChangeLog COPYING INSTALL NEWS README
%{_sysconfdir}/gconf/schemas/*.schemas
%{_bindir}/gnome-launch-box
%{_datadir}/lb


