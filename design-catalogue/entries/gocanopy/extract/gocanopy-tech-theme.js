// React Theme — extracted from https://gocanopy.tech
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
 *   };
 *   fonts: {
    body: string;
    mono: string;
 *   };
 *   fontSizes: {
    '11': string;
    '12': string;
    '14': string;
    '16': string;
    '18': string;
    '20': string;
    '24': string;
    '36': string;
    '53': string;
    '81': string;
 *   };
 *   space: {
    '2': string;
    '24': string;
    '36': string;
    '48': string;
    '56': string;
    '60': string;
    '64': string;
    '71': string;
    '80': string;
    '88': string;
    '112': string;
    '128': string;
    '160': string;
    '175': string;
    '241': string;
    '320': string;
 *   };
 *   radii: {
    sm: string;
    md: string;
    lg: string;
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
    "primary": "#00ffbb",
    "secondary": "#14323a",
    "accent": "#00ff7f",
    "background": "#1a4145",
    "foreground": "#000000",
    "neutral50": "#f6f5f3",
    "neutral100": "#000000",
    "neutral200": "#ffffff",
    "neutral300": "#979797",
    "neutral400": "#cecece",
    "neutral500": "#e2dfdf"
  },
  "fonts": {
    "body": "'Season Serif', sans-serif",
    "mono": "'Test Sohne Mono', monospace"
  },
  "fontSizes": {
    "11": "11px",
    "12": "12px",
    "14": "14px",
    "16": "16px",
    "18": "18px",
    "20": "20px",
    "24": "24px",
    "36": "36px",
    "53": "53px",
    "81": "81px"
  },
  "space": {
    "2": "2px",
    "24": "24px",
    "36": "36px",
    "48": "48px",
    "56": "56px",
    "60": "60px",
    "64": "64px",
    "71": "71px",
    "80": "80px",
    "88": "88px",
    "112": "112px",
    "128": "128px",
    "160": "160px",
    "175": "175px",
    "241": "241px",
    "320": "320px"
  },
  "radii": {
    "sm": "4px",
    "md": "8px",
    "lg": "16px"
  },
  "shadows": {
    "sm": "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, oklab(0.298003 -0.0303611 -0.0234222 / 0.05) 0px 1px 3px 0px, oklab(0.298003 -0.0303611 -0.0234222 / 0.05) 0px 1px 2px -1px"
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
      "main": "#00ffbb",
      "light": "hsl(164, 100%, 65%)",
      "dark": "hsl(164, 100%, 35%)"
    },
    "secondary": {
      "main": "#14323a",
      "light": "hsl(193, 49%, 30%)",
      "dark": "hsl(193, 49%, 10%)"
    },
    "background": {
      "default": "#1a4145",
      "paper": "#000000"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#f6f5f3"
    }
  },
  "typography": {
    "h1": {
      "fontSize": "36px",
      "fontWeight": "400",
      "lineHeight": "64px"
    },
    "h2": {
      "fontSize": "24px",
      "fontWeight": "400",
      "lineHeight": "31.2px"
    },
    "h3": {
      "fontSize": "20px",
      "fontWeight": "400",
      "lineHeight": "20px"
    },
    "body1": {
      "fontSize": "18px",
      "fontWeight": "500",
      "lineHeight": "18px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": [
    "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.25) 0px 25px 50px -12px",
    "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 4.16px 6.24px -4.16px, rgba(0, 0, 0, 0.1) 0px 10.4px 15.6px -3.12px",
    "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.35) 0px 16px 40px 0px",
    "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 20px 25px -5px, rgba(0, 0, 0, 0.1) 0px 8px 10px -6px",
    "rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0) 0px 0px 0px 0px, rgba(0, 0, 0, 0.1) 0px 1px 3px 0px, rgba(0, 0, 0, 0.1) 0px 1px 2px -1px"
  ]
};

export default theme;
