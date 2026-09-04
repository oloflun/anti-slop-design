// React Theme — extracted from https://oma-operator.framer.website/
// Compatible with: Chakra UI, Stitches, Vanilla Extract, or any CSS-in-JS

/**
 * TypeScript type definition for this theme:
 *
 * interface Theme {
 *   colors: {
    primary: string;
    secondary: string;
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
    '14': string;
    '15': string;
    '16': string;
    '18': string;
    '20': string;
    '22': string;
    '26': string;
    '31': string;
    '37': string;
    '45': string;
    '64': string;
 *   };
 *   space: {
    '1': string;
    '32': string;
    '48': string;
    '61': string;
    '80': string;
    '99': string;
    '120': string;
 *   };
 *   radii: {
    sm: string;
    md: string;
    lg: string;
    full: string;
 *   };
 *   shadows: {
    sm: string;
    xs: string;
    md: string;
    xl: string;
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
    "primary": "#0000ee",
    "secondary": "#0eea8e",
    "background": "#08090a",
    "foreground": "#000000",
    "neutral50": "#000000",
    "neutral100": "#74797d",
    "neutral200": "#fafafa",
    "neutral300": "#d4d6d8",
    "neutral400": "#f4f5f5",
    "neutral500": "#08090a",
    "neutral600": "#a1a5aa",
    "neutral700": "#181a1b",
    "neutral800": "#e4e6e7",
    "neutral900": "#52575b"
  },
  "fonts": {
    "body": "'Inter', sans-serif",
    "mono": "'Geist Mono', monospace"
  },
  "fontSizes": {
    "13": "13px",
    "14": "14px",
    "15": "15px",
    "16": "16px",
    "18": "18px",
    "20": "20px",
    "22": "22px",
    "26": "26px",
    "31": "31px",
    "37": "37px",
    "45": "45px",
    "64": "64px"
  },
  "space": {
    "1": "1px",
    "32": "32px",
    "48": "48px",
    "61": "61px",
    "80": "80px",
    "99": "99px",
    "120": "120px"
  },
  "radii": {
    "sm": "4px",
    "md": "8px",
    "lg": "11px",
    "full": "100px"
  },
  "shadows": {
    "sm": "rgb(0, 0, 0) 0px 0px 0px 1px inset",
    "xs": "rgba(46, 255, 157, 0.3) 0px 0px 3px 0px, rgba(255, 255, 255, 0.2) 0px 2px 7px 0px",
    "md": "rgba(0, 0, 0, 0.1) 0px 4px 10px 0px",
    "xl": "rgba(0, 0, 0, 0.37) -62px 16px 141px 0px, rgba(0, 0, 0, 0.32) -247px 64px 250px 0px, rgba(0, 0, 0, 0.19) -557px 145px 250px 0px, rgba(0, 0, 0, 0.06) -990px 257px 250px 0px, rgba(0, 0, 0, 0.01) -1546px 402px 250px 0px"
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
      "main": "#0000ee",
      "light": "hsl(240, 100%, 62%)",
      "dark": "hsl(240, 100%, 32%)"
    },
    "secondary": {
      "main": "#0eea8e",
      "light": "hsl(155, 89%, 64%)",
      "dark": "hsl(155, 89%, 34%)"
    },
    "background": {
      "default": "#08090a",
      "paper": "#0d0f0f"
    },
    "text": {
      "primary": "#000000",
      "secondary": "#08090a"
    }
  },
  "typography": {
    "fontFamily": "'Times New Roman', sans-serif",
    "h1": {
      "fontSize": "37px",
      "fontWeight": "500",
      "lineHeight": "40.7px"
    },
    "h2": {
      "fontSize": "26px",
      "fontWeight": "500",
      "lineHeight": "32.5px"
    },
    "h3": {
      "fontSize": "22px",
      "fontWeight": "500",
      "lineHeight": "28.6px"
    }
  },
  "shape": {
    "borderRadius": 8
  },
  "shadows": [
    "rgb(0, 0, 0) 0px 0px 0px 1px inset",
    "rgba(0, 0, 0, 0.17) 0px 0.602187px 1.56569px -1.5px, rgba(0, 0, 0, 0.14) 0px 2.28853px 5.95019px -3px, rgba(0, 0, 0, 0.02) 0px 10px 26px -4.5px",
    "rgba(255, 255, 255, 0.3) 0px 0px 3px 0px, rgba(255, 255, 255, 0.2) 0px 2px 7px 0px",
    "rgba(46, 255, 157, 0.3) 0px 0px 3px 0px, rgba(255, 255, 255, 0.2) 0px 2px 7px 0px",
    "rgba(0, 0, 0, 0.1) 0px 4px 10px 0px"
  ]
};

export default theme;
