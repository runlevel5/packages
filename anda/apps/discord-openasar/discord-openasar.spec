%define debug_package %{nil}

Name:           discord-openasar
Version:        0.0.24
Release:        1%{?dist}
Summary:        OpenAsar is a rewrite of part of Discord's desktop code, making it snappier and include more features like further customization and theming
License:        MIT and https://discord.com/terms
URL:            https://github.com/GooseMod/OpenAsar
Source0:        https://dl.discordapp.net/apps/linux/%{version}/discord-%{version}.tar.gz
Source1:        %{url}/releases/download/nightly/app.asar
Group:          Applications/Internet
Requires:       libatomic, glibc, alsa-lib, GConf2, libnotify, nspr >= 4.13, nss >= 3.27, libstdc++, libX11 >= 1.6, libXtst >= 1.2, libappindicator, libcxx, libXScrnSaver
ExclusiveArch:  x86_64

%description
%{summary}.

%prep
%autosetup -n Discord

%build
sed "s@discord@discord-openasar@g" discord.desktop > a
sed "s@Discord@Discord OpenAsar@g" a > discord.desktop

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}%{_datadir}/discord-openasar
cp -rv * %{buildroot}%{_datadir}/discord-openasar
mkdir -p %{buildroot}%{_datadir}/applications/
mkdir -p %{buildroot}%{_datadir}/pixmaps
install discord.desktop %{buildroot}%{_datadir}/applications/discord-openasar.desktop
install discord.png %{buildroot}%{_datadir}/pixmaps/discord-openasar.png
cp -v %{SOURCE1} %{buildroot}%{_datadir}/discord-openasar/resources/app.asar
chmod o+w %{buildroot}%{_datadir}/discord-openasar/resources -R


%files
%{_datadir}/discord-openasar/
%{_datadir}/applications/discord-openasar.desktop
%{_datadir}/pixmaps/discord-openasar.png


%changelog
* Sat Jan 21 2023 windowsboy111 <windowsboy111@fyralabs.com> - 0.0.38-1
- Initial package
