// React Theme — extracted from https://www.sanity.io
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
    accent: string;
    background: string;
    foreground: string;
    neutral50: string;
    neutral100: string;
    neutral200: string;
    neutral300: string;
    neutral400: string;
    neutral500: string;
    neutral600: string;
    neutral700: string;
    neutral800: string;
    neutral900: string;
 *   };
 *   fonts: {
    body: string;
    mono: string;
 *   };
 *   fontSizes: {
    '13': string;
    '15': string;
    '16': string;
    '18': string;
    '20': string;
    '24': string;
    '32': string;
    '38': string;
    '48': string;
    '60': string;
    '72': string;
    '112': string;
 *   };
 *   space: {
    '1': string;
    '32': string;
    '48': string;
    '64': string;
    '90': string;
    '103': string;
    '116': string;
    '127': string;
    '148': string;
    '161': string;
    '233': string;
    '256': string;
    '278': string;
    '340': string;
 *   };
 *   radii: {
    sm: string;
    md: string;
    lg: string;
    full: string;
 *   };
 *   shadows: {
    sm: string;
 *   };
 *   states: {
 *     hover: { opacity: number };
 *     focus: { opacity: number };
 *     active: { opacity: number };
 *     disabled: { opacity: number };
 *   };
 * }
 */

export const theme = {
  "colors": {
    "primary": "#0052ef",
    "secondary": "#9ecbff",
    "accent": "#ff5500",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#ffffff",
    "neutral100": "#0b0b0b",
    "neutral200": "#e1e4e8",
    "neutral300": "#000000",
    "neutral400": "#797979",
    "neutral500": "#b9b9b9",
    "neutral600": "#353535",
    "neutral700": "#212121",
    "neutral800": "#6a737d",
    "neutral900": "#4a4a4a"
  },
  "fonts": {
    "body": "'Helvetica', sans-serif",
    "mono": "'IBM Plex Mono-c20ba633a65a8c57', monospace"
  },
  "fontSizes": {
    "13": "13px",
    "15": "15px",
    "16": "16px",
    "18": "18px",
    "20": "20px",
    "24": "24px",
    "32": "32px",
    "38": "38px",
    "48": "48px",
    "60": "60px",
    "72": "72px",
    "112": "112px"
  },
  "space": {
    "1": "1px",
    "32": "32px",
    "48": "48px",
    "64": "64px",
    "90": "90px",
    "103": "103px",
    "116": "116px",
    "127": "127px",
    "148": "148px",
    "161": "161px",
    "233": "233px",
    "256": "256px",
    "278": "278px",
    "340": "340px"
  },
  "radii": {
    "sm": "3px",
    "md": "6px",
    "lg": "11px",
    "full": "99999px"
  },
  "shadows": {
    "sm": "rgb(53, 53, 53) 0px 0px 0px 1px inset"
  },
  "states": {
    "hover": {
      "opacity": 0.08
    },
    "focus": {
      "opacity": 0.12
    },
    "active": {
      "opacity": 0.16
    },
    "disabled": {
      "opacity": 0.38
    }
  }
};

// MUI v5 theme
export const muiTheme = {
  "palette": {
    "primary": {
      "main": "#0052ef",
      "light": "hsl(219, 100%, 62%)",
      "dark": "hsl(219, 100%, 32%)"
    },
    "secondary": {
      "main": "#9ecbff",
      "light": "hsl(212, 100%, 95%)",
      "dark": "hsl(212, 100%, 66%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#121923"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#0b0b0b"
    }
  },
  "typography": {
    "fontFamily": "'Helvetica', sans-serif",
    "h1": {
      "fontSize": "32px",
      "fontWeight": "425",
      "lineHeight": "35.2px"
    }
  },
  "shape": {
    "borderRadius": 6
  },
  "shadows": [
    "rgb(53, 53, 53) 0px 0px 0px 1px inset"
  ]
};

export default theme;
