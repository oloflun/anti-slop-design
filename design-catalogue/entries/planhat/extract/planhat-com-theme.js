// React Theme — extracted from https://www.planhat.com
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
 *   };
 *   fontSizes: {
    '13': string;
    '14': string;
    '16': string;
    '18': string;
    '20': string;
    '21': string;
    '24': string;
    '32': string;
    '48': string;
    '60': string;
    '72': string;
    '117.101': string;
 *   };
 *   space: {
    '1': string;
    '24': string;
    '30': string;
    '36': string;
    '40': string;
    '46': string;
    '64': string;
    '72': string;
    '91': string;
    '96': string;
    '120': string;
 *   };
 *   radii: {
    xs: string;
    sm: string;
    md: string;
    full: string;
 *   };
 *   shadows: {
    xs: string;
    md: string;
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
    "primary": "#c0ff66",
    "secondary": "#0000ee",
    "accent": "#22c55e",
    "background": "#ffffff",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#ffffff",
    "neutral200": "#403a35",
    "neutral300": "#767676",
    "neutral400": "#9e9d9b",
    "neutral500": "#575551"
  },
  "fonts": {
    "body": "'ABC Arizona Flare Regular', sans-serif"
  },
  "fontSizes": {
    "13": "13px",
    "14": "14px",
    "16": "16px",
    "18": "18px",
    "20": "20px",
    "21": "21px",
    "24": "24px",
    "32": "32px",
    "48": "48px",
    "60": "60px",
    "72": "72px",
    "117.101": "117.101px"
  },
  "space": {
    "1": "1px",
    "24": "24px",
    "30": "30px",
    "36": "36px",
    "40": "40px",
    "46": "46px",
    "64": "64px",
    "72": "72px",
    "91": "91px",
    "96": "96px",
    "120": "120px"
  },
  "radii": {
    "xs": "1px",
    "sm": "4px",
    "md": "8px",
    "full": "999px"
  },
  "shadows": {
    "xs": "rgba(0, 0, 0, 0.08) 0px -1px 0px 0px, rgba(0, 0, 0, 0.06) 0px -8px 32px 0px",
    "md": "rgba(0, 0, 0, 0.12) 0px 0px 10px 0px"
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
      "main": "#c0ff66",
      "light": "hsl(85, 100%, 85%)",
      "dark": "hsl(85, 100%, 55%)"
    },
    "secondary": {
      "main": "#0000ee",
      "light": "hsl(240, 100%, 62%)",
      "dark": "hsl(240, 100%, 32%)"
    },
    "background": {
      "default": "#ffffff",
      "paper": "#000000"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#ffffff"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "h1": {
      "fontSize": "32px",
      "fontWeight": "400",
      "lineHeight": "38.4px"
    },
    "h2": {
      "fontSize": "24px",
      "fontWeight": "400",
      "lineHeight": "31.2px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": [
    "rgba(0, 0, 0, 0.08) 0px -1px 0px 0px, rgba(0, 0, 0, 0.06) 0px -8px 32px 0px",
    "rgba(0, 0, 0, 0.12) 0px 0px 10px 0px"
  ]
};

export default theme;
